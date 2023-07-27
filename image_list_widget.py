from enum import Enum

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QListWidget, QListWidgetItem
from tinydb.table import Document

from image_item_widget import ThumbnailWidget

from progress_dialog import LongMethodCall
from image_model import ImageModel

import asyncio


class SortType(Enum):
    Name = 1 << 0
    CreationDate = 1 << 1


class ImageListWidget(QListWidget):
    updated = Signal(int)
    set_max_signal = Signal(int)
    start_signal = Signal(object)
    done_signal = Signal(object)

    model_info_changed = Signal(ImageModel)

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.folder_path = None
        self.new_images_list = None
        self.images_dict = {}
        self.done_signal.connect(self._on_finish_loading)


    def sort(self, by: SortType, order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        if (by == SortType.Name):
            self._sort_by_name(order)
        elif (by == SortType.CreationDate):
            self._sort_by_date(order)

    @Slot(list)
    def on_db_updated(self, images_list: list) -> None:
        self.new_images_list = images_list
        self._set_items_hidden()
        LongMethodCall.launch_long_method(self, "_load_async")

    @Slot(QListWidgetItem)
    def on_list_view_item_changed(self, item: QListWidgetItem):
        thumbnail: ThumbnailWidget = item.listWidget().itemWidget(item)
        model = thumbnail.model()
        self.model_info_changed.emit(model)

    async def _load_async(self) -> None:
        self.set_max_signal.emit(len(self.new_images_list))
        for image_info, count in zip(self.new_images_list, range(len(self.new_images_list))):
            await asyncio.sleep(0.0001)
            self._load_image(image_info)
            self.updated.emit(count)
        self.done_signal.emit(self)

    def _load_image(self, image_info: Document) -> ThumbnailWidget:
        if image_info.doc_id not in self.images_dict.keys():
            image_model = ImageModel(image_info)
            thumbnail_widget = ThumbnailWidget(image_model)
            item = QListWidgetItem(self)
            item.setSizeHint(thumbnail_widget.sizeHint())
            data = {'model': image_model, 'widget': thumbnail_widget, 'item': item}
            self.images_dict[image_info.doc_id] = data
            self.setItemWidget(item, thumbnail_widget)
        else:
            data = self.images_dict[image_info.doc_id]
            data['item'].setHidden(False)
            thumbnail_widget = data['widget']

        return thumbnail_widget

    def _sort_by_name(self, order: Qt.SortOrder) -> None:
        self.sortItems()

    @Slot()
    def _on_finish_loading(self):
        self.sort(by=SortType.Name)
        if self.currentItem():
            self.scrollToItem(self.currentItem())

    def _set_items_hidden(self):
        for key, value in self.images_dict.items():
            value['item'].setHidden(True)
