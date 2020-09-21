# coding: utf-8


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def length(self):
        curr = self.head
        len_ = 0

        while curr is not None:
            curr = curr.next
            len_ += 1

        return len_

    def search(self, item):
        curr = self.head
        found = False

        while not found and curr is not None:
            if curr.data == item:
                found = True
            else:
                curr = curr.next

        return found

    def access(self, pos):
        if pos > self.length() or pos < 0:
            return 'pos parameter not within bounds of list.'

        curr = self.head
        index = 0

        while index < pos:
            curr = curr.next
            index += 1

        return curr.data

    def append(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def insert(self, pos, item):
        if pos > self.length() or pos < 0:
            return 'pos parameter not within bounds of list.'

        curr = self.head
        prev = None
        index = 0

        while index < pos:
            curr, prev = curr.next, curr
            index += 1

        temp = Node(item)

        if curr is self.head:
            if self.head is None:
                self.head = temp
            else:
                temp.next = self.head
                self.head = temp
        else:
            temp.next = prev.next
            prev.next = temp

    def delete(self, item):
        curr = self.head
        prev = None

        while curr is not None and curr.data != item:
            prev = curr
            curr = curr.next

        if curr is None:
            return 'Item not found.'
        elif curr is self.head:
            self.head = curr.next
        else:
            prev.next = curr.next

    def __iter__(self):
        curr = self.head

        if curr:
            while curr.next is not None:
                yield curr
                curr = curr.next
            yield curr

    def __str__(self):
        return '(Head) {}-> None'.format('->'.join(map(str, self)))


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def length(self):
        curr = self.head
        len_ = 0

        while curr is not None:
            curr = curr.next
            len_ += 1

        return len_

    def search(self, item):
        curr = self.head
        found = False
        
        while not found and curr is not None:
            if curr.data == item:
                found = True
            else:
                curr = curr.next

        return found

    def access(self, pos):
        if pos > self.length() or pos < 0:
            return 'pos parameter not within bounds of list.'

        curr = self.head
        index = 0

        while index < pos:
            curr = curr.next
            index += 1

        return curr.data

    def append(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def insert(self, pos, item):
        if pos > self.length() or pos < 0:
            return 'pos parameter not within bounds of list.'

        curr = self.head
        prev = None
        index = 0

        while index < pos:
            curr, prev = curr.next, curr
            index += 1

        temp = Node(item)

        if curr is self.head:
            if self.head is None:
                self.head = temp
            else:
                temp.next = self.head
                self.head.prev = temp
                self.head = temp
        else:
            temp.next = prev.next
            temp.prev = prev
            prev.next = temp

    def delete(self, item):
        curr = self.head
        prev = None

        while curr is not None and curr.data != item:
            prev = curr
            curr = curr.next

        if curr is None:
            return 'Item not found.'
        elif curr is self.head:
            self.head = curr.next

            if self.head is not None:
                self.head.prev = None
        else:
            prev.next = curr.next
            
            if curr.next is not None:
                curr.next.prev = prev

    def __iter__(self):
        curr = self.head

        if curr:
            while curr.next is not None:
                yield curr
                curr = curr.next
            yield curr

    def __str__(self):
        return '(Head) {}-> None'.format('<->'.join(map(str, self)))


class Node:

    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)
