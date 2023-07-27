import sys
from PySide6.QtWidgets import QApplication

from app_window import AppWindow


def quit_app():
    app.quit()


def main():
    main_window = AppWindow()
    main_window.close_action.triggered.connect(quit_app)
    main_window.show()
    return app.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(main())
