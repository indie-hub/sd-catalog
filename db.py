import os
import asyncio
import json

from PySide6.QtCore import QObject, Signal, Slot

from tinydb import TinyDB, Query
from PIL import Image

from image_model import ImageModel


def _get_dictionary_items(from_dict: dict, to_dict: dict) -> None:
    for key, value in from_dict.items():
        try:
            eval_value = json.loads(value)
        except Exception:
            to_dict[key] = value
        else:
            try:
                items = eval_value.items()
            except (AttributeError, TypeError) as e:
                to_dict[key] = value
            else:
                to_dict[key] = {}
                _get_dictionary_items(eval_value, to_dict[key])


class ImagesDatabase(QObject):
    updated = Signal(int)
    set_max_signal = Signal(int)
    start_signal = Signal(object)
    done_signal = Signal(object)

    db_updated = Signal(list)

    def __init__(self, folder_path, db_path):
        super().__init__()
        self.db = None
        self.db_path = db_path
        self.folder_path = folder_path
        self.query_fields = {}

    async def load_async(self) -> None:
        # with TinyDB(Path(self.db_path), access_mode="r+", storage=BetterJSONStorage) as self.db:
        self.db = TinyDB(os.path.join(self.folder_path, self.db_path))
        self._mark_all_image_as_unseen()
        file_names = os.listdir(self.folder_path)
        self.set_max_signal.emit(len(file_names))
        for file_name, count in zip(file_names, range(len(file_names))):
            await asyncio.sleep(0.0001)
            self._insert_image(self.folder_path, file_name)
            self.updated.emit(count)
        self.done_signal.emit(self)
        self.db_updated.emit(self.db.all())

    def _insert_image(self, folder_path: str, file_name: str) -> None:
        file_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(file_path):
            return
        try:
            with Image.open(file_path) as image:
                db_image = self._image_in_database(file_name)
                if not db_image:
                    data = {"filename": file_name, "name": os.path.basename(image.filename), "size": image.size,
                            "ctime": os.path.getctime(image.filename), "favourite": False}
                    _get_dictionary_items(image.info, data)
                    data["seen"] = True

                    self.db.insert(data)
                else:
                    self.db.update({'seen': True}, doc_ids=[db_image.doc_id])

        except Exception as e:
            pass

    def _image_in_database(self, filename: str) -> object:
        return self.db.get(Query().filename == filename)

    def _mark_all_image_as_unseen(self):
        self.db.update({'seen': False})

    @Slot(ImageModel)
    def on_image_updated(self, image: ImageModel):
        self.db.update({"favourite": image.is_favorite()}, doc_ids=[image.id])
        self._emit_filtered()

    def filter_favorites(self, checked):
        self._toggle_query_field("favourite", checked, checked)
        self._emit_filtered()

    def filter_by_path(self, path, text, checked) -> None:
        self._toggle_query_field(path, checked, text)
        self._emit_filtered()

    def _toggle_query_field(self, field: str, checked: bool, value: object) -> None:
        if not checked:
            if field in self.query_fields:
                del self.query_fields[field]
            return
        self.query_fields[field] = value

    def _emit_filtered(self):
        print(self.query_fields)
        query_result = self.db.search(Query().fragment(self.query_fields))
        self.db_updated.emit(query_result)


def main() -> int:
    db = ImagesDatabase("image_db.json")

    return 0


if __name__ == "__main__":
    main()
