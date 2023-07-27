from PySide6.QtCore import Slot
from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem

from image_model import ImageModel


class MetadataTree(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    @Slot(ImageModel)
    def on_list_view_item_changed(self, item: ImageModel):
        self.clear()
        self._set_data(item)
        self.expandAll()

    @Slot()
    def on_app_ready(self):
        self.setHeaderLabels(['Key', 'Value'])

    def _set_data(self, model: ImageModel) -> None:
        metadata = model.sd_metadata()
        self._add_tree_level(self, metadata)

    def _add_tree_level(self, parent, metadata) -> None:
        for key, value in metadata.items():
            tree_node = QTreeWidgetItem(parent, [str(key)])
            try:
                items = value.items()
            except (AttributeError, TypeError) as e:
                tree_node.setData(1, 0, value)
            else:
                self._add_tree_level(tree_node, value)
