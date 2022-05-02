'''
2 створити контекст менеджер, якому можна передати ім'я папки i назви файлів.
    На вході він створить папку з усіма файлами
завдання зробити через клас та через генератор
os.mkdir(path, mode=0o777, *, dir_fd=None) - создаёт директорию. OSError, если директория существует.
'''
import os
from contextlib import contextmanager


class OpenFile:
    def __init__(self, filename, mode, filename2):
        self.filename = filename
        self.mode = mode
        self.name2 = filename2

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
