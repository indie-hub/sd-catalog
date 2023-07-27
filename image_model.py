import re
from PIL import Image
from tinydb.table import Document


class ImageModel:
    THUMBNAIL_WIDTH = 100

    def __init__(self, image_info: Document):
        self._image_info = image_info
        self._image = Image.open(image_info["filename"])
        self._thumbnail = self._image.copy()
        self.id = image_info.doc_id

        thumbnail_height = int((ImageModel.THUMBNAIL_WIDTH / float(self._image.width)) * self._image.height)
        thumbnail_size = (ImageModel.THUMBNAIL_WIDTH, thumbnail_height)

        self._thumbnail.thumbnail(thumbnail_size)

        self._prompt = None
        self._negative = None

        matches = re.match(r"(.*)\[(.*)\]$|(.*)", self._image_info["sd-metadata"]["image"]["prompt"])
        self._image_sd_data = self._image_info["sd-metadata"]["image"]
        self._sd_data = self._image_info["sd-metadata"]

        self._prompt = matches.group(1) if matches.group(1) else matches.group(3)
        self._negative = matches.group(2) if matches.group(2) else None

    def image(self) -> Image.Image:
        return self._image

    def thumbnail(self) -> Image.Image:
        return self._thumbnail

    def width(self) -> int:
        return self._image.width

    def height(self) -> int:
        return self._image.height

    def sd_metadata(self) -> dict:
        return self._image_info["sd-metadata"]

    def prompt(self) -> str:
        return self._prompt

    def negative_prompt(self) -> str:
        return self._negative

    def model(self):
        return self._sd_data["model_weights"]

    def cfg(self):
        return self._image_sd_data["cfg_scale"]

    def steps(self):
        return self._image_sd_data["steps"]

    def sampler(self):
        return self._image_sd_data["sampler"]

    def threshold(self):
        return self._image_sd_data["threshold"]

    def perlin(self):
        return self._image_sd_data["perlin"]

    def seed(self):
        return self._image_sd_data["seed"]

    def hires_fix(self):
        return self._image_sd_data["hires_fix"]

    def seamless(self):
        return self._image_sd_data["seamless"]

    def type(self):
        return self._image_sd_data["type"]

    def postprocessing(self):
        return self._image_sd_data["postprocessing"]

    def is_favorite(self):
        return self._image_info["favourite"]

    def set_favourite(self, value: bool):
        self._image_info["favourite"] = value
