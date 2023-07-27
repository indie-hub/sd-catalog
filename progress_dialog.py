from PySide6.QtCore import Qt, Signal, Slot, QObject, QTimer
from PySide6.QtWidgets import QDialog, QProgressBar, QHBoxLayout, QSizePolicy

from asynchelper import AsyncHelper


class LongMethodCall(QObject):
    main_window = None

    @staticmethod
    def launch_long_method(obj: object, method_name: str, *args, **kwargs) -> None:
        if not (hasattr(obj, "start_signal") and isinstance(obj.start_signal, Signal)):
            print(f'{obj} has no signal start_signal')
            return
        if not (hasattr(obj, "done_signal") and isinstance(obj.done_signal, Signal)):
            print(f'{obj} has no signal done_signal')
            return
        if not (hasattr(obj, "updated") and isinstance(obj.updated, Signal)):
            print(f'{obj} has no signal updated')
            return
        if not (hasattr(obj, "set_max_signal") and isinstance(obj.set_max_signal, Signal)):
            print(f'{obj} has no signal set_max_signal')
            return

        progress = ProgressDialog(obj, LongMethodCall.main_window)
        method = getattr(obj, method_name)

        asynchelper = AsyncHelper()
        asynchelper.add_worker(obj, method)

        obj.start_signal.emit(obj)


class ProgressDialog(QDialog):

    def __init__(self, widget, parent=None):
        super().__init__(parent=parent)

        widget.set_max_signal.connect(self._on_set_max)
        widget.updated.connect(self._on_progress_signal)
        widget.done_signal.connect(self._on_finished)

        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.resize(568, 52)
        size_policy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setModal(True)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setObjectName(u"progressBar")
        self.progress_bar.setValue(0)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)

        self.horizontalLayout.addWidget(self.progress_bar)

        self.setWindowTitle("Progress")
        self.setModal(True)

        self.show()

    @Slot(int)
    def _on_progress_signal(self, value):
        self.progress_bar.setValue(value)

    @Slot(int)
    def _on_set_max(self, value):
        self.progress_bar.setMaximum(value)

    @Slot(object)
    def _on_finished(self):
        self.close()
