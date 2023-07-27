from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDockWidget

from image_model import ImageModel
from settings_window_ui import Ui_SettingsDock


class GenerationSettingsWindow(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_SettingsDock()
        self.ui.setupUi(self)

    @Slot(ImageModel)
    def on_list_view_item_changed(self, item: ImageModel) -> None:
        pass




