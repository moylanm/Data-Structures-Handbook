# coding: utf-8

class Array:

    def __init__(self):
        self.array = []

    def __getitem__(self, index):
        try:
            return self.array[index]
        except IndexError:
            return 'Index out of range.'

    def search(self, value):
        try:
            return self.array.index(value)
        except ValueError:
            return 'Value not found.'

    def append(self, value):
        self.array.append(value)

    def insert(self, index, value):
        self.array.insert(index, value)

    def delete(self, value):
        try:
            self.array.remove(value)
        except ValueError:
            return 'Value not found.'

    def __str__(self):
        return str(self.array)