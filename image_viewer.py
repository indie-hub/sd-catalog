from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsDropShadowEffect
from PySide6.QtGui import QPixmap
from PIL import Image, ImageQt

from image_model import ImageModel


class ImageViewer(QGraphicsView):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.last_mouse_pos = None
        self.setMouseTracking(True)

        self.setDragMode(QGraphicsView.RubberBandDrag)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

    def wheelEvent(self, event):
        # Zoom in/out using the mouse wheel
        zoom_factor = 1.2  # Adjust this value to control the zoom speed

        # Calculate the zoom factor based on the mouse wheel delta
        if event.angleDelta().y() > 0:
            zoom = zoom_factor
        else:
            zoom = 1 / zoom_factor

        # Perform the zoom transformation
        self.scale(zoom, zoom)

    def mousePressEvent(self, event):
        # Enable panning by capturing the initial mouse position
        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self.last_mouse_pos = event.pos()

    def mouseMoveEvent(self, event):
        # Pan the view by adjusting the scroll bars based on mouse movement
        if self.dragMode() == QGraphicsView.ScrollHandDrag:
            delta = self.last_mouse_pos - event.pos()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + delta.y())
            self.last_mouse_pos = event.pos()

    def mouseReleaseEvent(self, event):
        # Disable panning
        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.RubberBandDrag)
            self.viewport().setCursor(Qt.ArrowCursor)

    @Slot(ImageModel)
    def on_list_view_item_changed(self, item: ImageModel):
        self._set_image(item.image())

    def _set_image(self, image: Image.Image):
        self.scene.clear()

        pixmap = QPixmap.fromImage(ImageQt.ImageQt(image))

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)

        image_on_view = self.scene.addPixmap(pixmap)
        image_on_view.setGraphicsEffect(shadow)
