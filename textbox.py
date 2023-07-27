from PySide6.QtCore import Slot, QObject
from PySide6.QtWidgets import QPlainTextEdit, QLineEdit

from image_model import ImageModel


class TextBoxInfo(QObject):
    def __init__(self):
        self.field = None
        self.path = None

    def set_field(self, field: str) -> None:
        self.field = field

    def set_path(self, path: str) -> None:
        self.path = path

    def get_path(self) -> str:
        return self.path

    @Slot(ImageModel)
    def on_list_view_item_changed(self, item: ImageModel):
        text = None
        if hasattr(item, self.field):
            method = item.__getattribute__(self.field)
            text = method()
        self.set_text(text)

    def get_text(self):
        pass

    def set_text(self, text):
        pass


class TextBox(QPlainTextEdit, TextBoxInfo):
    def __int__(self, parent=None):
        super().__int__(parent)

    def set_text(self, text):
        self.setPlainText(str(text))

    def get_text(self):
        return self.toPlainText()


class LineEditBox(QLineEdit, TextBoxInfo):
    def __int__(self, parent=None):
        super().__int__(parent)

    def set_text(self, text):
        self.setText(str(text))

    def get_text(self):
        return self.text()
