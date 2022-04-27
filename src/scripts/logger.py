# -*- coding: utf-8 -*-

# shlom41k


class Logger:

    __file_name: str

    def __init__(self, file_name: str):
        self.__file_name = file_name
        # self.change_file(file_name)

    def __del__(self):
        pass

    def add(self, text: str):
        with open(self.__file_name, "a") as fs:
            fs.write(text + "\n")

    def read(self):
        with open(self.__file_name, "r") as fs:
            return fs.read()

    def change_file(self, new_name: str):
        self.__file_name = new_name


if __name__ == "__main__":
    pass
