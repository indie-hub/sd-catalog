from PySide6.QtCore import (Qt, QEvent, QObject, Signal, Slot)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)

import asyncio


class AsyncHelper(QObject):
    
    class ReenterQtObject(QObject):
        """ This is a QObject to which an event will be posted, allowing
            asyncio to resume when the event is handled. event.fn() is
            the next entry point of the asyncio event loop. """
        def event(self, event):
            if event.type() == QEvent.Type.User + 1:
                event.fn()
                return True
            return False

    class ReenterQtEvent(QEvent):
        """ This is the QEvent that will be handled by the ReenterQtObject.
            self.fn is the next entry point of the asyncio event loop. """
        def __init__(self, fn):
            super().__init__(QEvent.Type(QEvent.Type.User + 1))
            self.fn = fn
            
    _instance = None    
    _initialised = False
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AsyncHelper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if AsyncHelper._initialised:
            return
        
        super().__init__()
        self.reenter_qt = self.ReenterQtObject()
        
        self.loop = asyncio.new_event_loop()
        self.workers = {}

        self.done = False
        AsyncHelper._initialised = True

    def add_worker(self, worker, entry):
        work = {
            "worker": worker,
            "entry": entry,
            "done": False
        }
        
        self.workers[worker] = work
        
        if hasattr(worker, "start_signal") and isinstance(worker.start_signal, Signal):
            worker.start_signal.connect(self.on_worker_started)
        if hasattr(worker, "done_signal") and isinstance(worker.done_signal, Signal):
            worker.done_signal.connect(self.on_worker_done)
    

    @Slot(object)
    def on_worker_started(self, worker):
        """ To use asyncio and Qt together, one must run the asyncio
            event loop as a "guest" inside the Qt "host" event loop. """
            
        work = self.workers[worker]
        if not work["entry"]:
            raise Exception("No entry point for the asyncio event loop was set.")
        #asyncio.set_event_loop(self.loop)
        self.loop.create_task(work["entry"]())
        self.loop.call_soon(self.next_guest_run_schedule)
        self.done = False  # Set this explicitly as we might want to restart the guest run.
        if not self.loop.is_running():
            self.loop.run_forever()

    @Slot(object)
    def on_worker_done(self, worker):
        """ When all our current asyncio tasks are finished, we must end
            the "guest run" lest we enter a quasi idle loop of switching
            back and forth between the asyncio and Qt loops. We can
            launch a new guest run by calling launch_guest_run() again. """
        self.workers[worker]["done"] = True

    def continue_loop(self):
        """ This function is called by an event posted to the Qt event
            loop to continue the asyncio event loop. """
        if not self.done:
            self.loop.call_soon(self.next_guest_run_schedule)
            self.loop.run_forever()

    def next_guest_run_schedule(self):
        """ This function serves to pause and re-schedule the guest
            (asyncio) event loop inside the host (Qt) event loop. It is
            registered in asyncio as a callback to be called at the next
            iteration of the event loop. When this function runs, it
            first stops the asyncio event loop, then by posting an event
            on the Qt event loop, it both relinquishes to Qt's event
            loop and also schedules the asyncio event loop to run again.
            Upon handling this event, a function will be called that
            resumes the asyncio event loop. """
        self.loop.stop()
        QApplication.postEvent(self.reenter_qt, self.ReenterQtEvent(self.continue_loop))
