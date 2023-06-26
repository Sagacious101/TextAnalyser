import re
from pathlib import Path
from typing import NoReturn

import chardet
import pymorphy3


class TextAnalyzer:
    def __init__(self, file_path=None, pos=None) -> None:
        if not file_path:
            raise Exception("Ошибка! Не указан путь к файлу")
        self.file_path = Path(file_path)

        self.open_file()
        self.get_text()
        self.make_lower()
        self.clean_text()
        self.get_pos(pos)

    def open_file(self):
        try:
            file = open(self.file_path,'+r',encoding="utf-8")
            self.file = file
        except FileNotFoundError:
            raise FileNotFoundError("Ошибка! Файл не найден")

    def get_text(self) -> None:
        self.text = self.file.read()
        self.file.close()

    def check_empty_file(self):
        if not self.text:
            raise RuntimeError("Ошибка! Файл пуст")

    def make_lower(self) -> None:
        self.check_empty_file()
        self.text = self.text.lower()

    def clean_text(self) -> None:
        self.check_empty_file()
        self.text = re.findall(r"[А-Яа-яёЁ]+", self.text)

    def get_pos(self, pos: list = None) -> None:
        self.check_empty_file()
        if not pos:
            raise Exception("Ошибка! Не указана часть речи")
        mngr = pymorphy3.MorphAnalyzer()
        all_words = {mngr.parse(i)[0].normal_form: mngr.parse(i)[0].tag.POS for i in self.text}
        if len(pos) == 1:
            print(f"{pos[0]}: {[i for i in all_words if all_words.get(i) == pos[0]]}")
        else:
            for part in pos:
                print(f"{part}: {[i for i in all_words if all_words.get(i) == part]}")

    def print_text(self) -> None:
        print(self.text)


TextAnalyzer(file_path="./text.txt", pos=["NOUN"])
