'''
1 створити контекст менеджер, якому можна передати ім'я файла i вміст. На вході він його створить з вмістом
Завдання зробити через клас та через генератор
'''
import os
from contextlib import contextmanager


class OpenFile:
    def __init__(self, filename, mode, cont):
        self.filename = filename
        self.mode = mode
        self.cont = cont

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@contextmanager
def open_file(filename, mode, cont):
    f = open(filename, mode)
    yield f
    f.close()

    with open('test.txt', 'a') as f:
        f.write(cont)
        print('wrote to file ----- Done')
