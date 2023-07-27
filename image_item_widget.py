import os
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QPainter, QPaintEvent
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PIL import ImageQt

from image_model import ImageModel

import resources_rc


class ThumbnailWidget(QWidget):

    def __init__(self, model: ImageModel):
        super().__init__()
        self._model = model
        layout = QVBoxLayout()

        label = StaredImage(self._model)
        layout.addWidget(label)

        self.setLayout(layout)

    def name(self) -> str:
        return self._model.name()

    def model(self) -> ImageModel:
        return self._model


class StaredImage(QWidget):
    star: QPixmap = None

    def __init__(self, image_model: ImageModel):
        super().__init__()

        self.model = image_model
        self.thumbnail = ImageQt.ImageQt(image_model.thumbnail())
        if not StaredImage.star:
            start_image = QPixmap(u':/image/icons/star-icon.png')
            StaredImage.star = start_image.scaledToWidth(20)
        self.image_position = self.thumbnail.rect().topLeft() + QPoint(5, 5)
        self.setMinimumHeight(self.thumbnail.rect().height())

    def paintEvent(self, e: QPaintEvent) -> None:
        painter: QPainter = QPainter(self)
        start_point: QPoint = QPoint(e.rect().width() * 0.5 - self.thumbnail.rect().width() * 0.5, 0)

        painter.drawImage(start_point, self.thumbnail)
        if self.model.is_favorite():
            painter.drawPixmap(self.image_position + start_point, StaredImage.star)

        # End the painting
        painter.end()
