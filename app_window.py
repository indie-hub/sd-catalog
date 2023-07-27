import json

from PySide6.QtCore import Signal, Slot, QFile, QIODevice, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QFileDialog, QWidget, QToolButton, QButtonGroup, QAbstractButton

from image_model import ImageModel
from mainwindow_ui import Ui_MainWindow

from db import ImagesDatabase
from progress_dialog import LongMethodCall
from textbox import TextBoxInfo


class AppWindow(QMainWindow):
    filter_buttons_group: QButtonGroup
    FILTER_POSTFIX = "Filter"
    TEXTBOX_POSTFIX = "Text"

    app_ready = Signal()
    item_updated = Signal(ImageModel)

    def __init__(self):
        super().__init__()

        self.active_item: ImageModel = None
        self.db = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._set_action_listeners()
        self._prepare_filter_buttons()

        self.close_action = self.ui.actionE_xit
        LongMethodCall.main_window = self

        self.app_ready.emit()

    def _prepare_filter_buttons(self):
        self.filter_text_map = {}
        self.filter_buttons_group = QButtonGroup()
        self.filter_buttons_group.setExclusive(False)
        self._set_filter_buttons(self, self.ui.imageList.model_info_changed)
        self._set_filter_buttons(self.ui.SettingsDock, self.ui.imageList.model_info_changed)
        self.filter_buttons_group.buttonToggled.connect(self._on_button_group_toggle)

    def _set_action_listeners(self):
        self.ui.actionOpen_Folder.triggered.connect(self._on_open_folder_action)

        self.ui.imageList.itemClicked.connect(self.ui.imageList.on_list_view_item_changed)

        self.ui.imageList.model_info_changed.connect(self._on_list_view_item_changed)
        self.ui.imageList.model_info_changed.connect(self.ui.imageView.on_list_view_item_changed)
        self.ui.imageList.model_info_changed.connect(self.ui.metadataWidget.on_list_view_item_changed)
        self.ui.imageList.model_info_changed.connect(self.ui.SettingsDock.on_list_view_item_changed)

        self.app_ready.connect(self.ui.metadataWidget.on_app_ready)

        self.ui.actionAdd_to_Favorites.triggered.connect(self._on_favourites_triggered)
        self.ui.actionShow_Favorites_Only.triggered.connect(self._on_show_favourites_only)

    def _on_open_folder_action(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_path:
            self.db = ImagesDatabase(folder_path, "images.json")

            self.db.db_updated.connect(self._on_db_updated)
            self.db.db_updated.connect(self.ui.imageList.on_db_updated)
            self.item_updated.connect(self.db.on_image_updated)

            LongMethodCall.launch_long_method(self.db, "load_async")

    def _set_filter_buttons(self, widget: QWidget, connect_to: Signal):
        # Read json date from file
        resource_file = QFile(':/configuration/button_config.json')
        button_data = []

        icon = QIcon()
        icon.addFile(u"icons/filter.svg", QSize(), QIcon.Normal, QIcon.Off)

        if resource_file.open(QIODevice.ReadOnly | QIODevice.Text):
            resource_data = resource_file.readAll()
            resource_string = str(resource_data, encoding='utf-8')
            button_data = json.loads(resource_string)

        for button in button_data:
            if not button["window"] == widget.objectName():
                continue

            textbox_name = f'{button["name"]}{AppWindow.TEXTBOX_POSTFIX}'
            text: TextBoxInfo = widget.findChild(TextBoxInfo, textbox_name)
            if not text:
                print(f'Could not find: {textbox_name}')
                continue
            text.set_field(button["method"])
            text.set_path(button["db_path"])
            connect_to.connect(text.on_list_view_item_changed)

            filter_button_name = f'{button["name"]}{AppWindow.FILTER_POSTFIX}'
            filter_button: QToolButton = widget.findChild(QToolButton, filter_button_name)
            if filter_button:
                filter_button.setIcon(icon)
                filter_button.setIconSize(QSize(18, 18))
                filter_button.setCheckable(True)
                filter_button.setAutoRaise(True)
                self.filter_buttons_group.addButton(filter_button)
                self.filter_text_map[filter_button] = text

    @Slot(ImageModel)
    def _on_list_view_item_changed(self, item: ImageModel) -> None:
        self.ui.actionAdd_to_Favorites.setChecked(item.is_favorite())
        self.active_item = item

    @Slot(bool)
    def _on_favourites_triggered(self, checked: bool) -> None:
        if not self.active_item:
            return
        self.active_item.set_favourite(checked)
        self.item_updated.emit(self.active_item)

    @Slot(bool)
    def _on_show_favourites_only(self, checked: bool) -> None:
        self.db.filter_favorites(checked)

    @Slot(list)
    def _on_db_updated(self, images) -> None:
        self.active_list = images

    @Slot(QAbstractButton, bool)
    def _on_button_group_toggle(self, button: QAbstractButton, checked: bool) -> None:
        text_info: TextBoxInfo = self.filter_text_map[button]
        text = text_info.get_text()
        path = text_info.get_path()

        self.db.filter_by_path(path, text, checked)
