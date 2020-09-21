# coding: utf-8


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else 'Stack is empty.'

    def peek(self):
        return self.stack[-1] if not self.is_empty() else 'Stack is empty.'

    def is_empty(self):
        return self.stack == []

    def __str__(self):
        return '(Base) {} (Top)'.format(self.stack)