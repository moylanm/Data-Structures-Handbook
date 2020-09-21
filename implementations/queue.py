# coding: utf-8

    
class Queue:

    def __init__(self):
        self.queue = CircularlyLinkedList()

    def peek(self):
        return self.queue.peek_head()

    def enqueue(self, item):
        self.queue.add_rear(item)

    def dequeue(self):
        return self.queue.pop_front()

    def __str__(self):
        return '(Back) {} (Front)'.format(' '.join(map(str, self.queue)))


class Deque:

    def __init__(self):
        self.deque = CircularlyLinkedList()

    def peek_front(self):
        return self.deque.peek_head()

    def peek_rear(self):
        return self.deque.peek_tail()

    def enqueue_front(self, item):
        self.deque.add_front(item)

    def enqueue_rear(self, item):
        self.deque.add_rear(item)

    def dequeue_front(self):
        return self.deque.pop_front()

    def dequeue_rear(self):
        return self.deque.pop_rear()

    def __str__(self):
        return '(Back) {} (Front)'.format(' '.join(map(str, self.deque)))


class CircularlyLinkedList:
    
    def __init__(self):
        self.tail = None

    def peek_head(self):
        return self.tail.prev if self.tail else None

    def peek_tail(self):
        return self.tail if self.tail else None

    def add_front(self, item):
        if not self.tail:
            self.tail = Node(item)
            self.tail.prev = self.tail
            self.tail.next = self.tail
        else:
            head = self.tail.prev
            temp = Node(item, prev=head, next=self.tail)

            self.tail.prev = temp
            head.next = temp

    def add_rear(self, item):
        if not self.tail:
            self.tail = Node(item)
            self.tail.next = self.tail
            self.tail.prev = self.tail
        else:
            head = self.tail.prev
            temp = Node(item, prev=head, next=self.tail)

            self.tail.prev = temp
            self.tail = temp
            head.next = temp

    def pop_front(self):
        if not self.tail:
            return None
        
        head = self.tail.prev

        if head is self.tail:
            self.tail = None
        else:
            self.tail.prev = head.prev
            head.prev.next = self.tail

        return head

    def pop_rear(self):
        if not self.tail:
            return None

        head = self.tail.prev
        tail = self.tail

        if head is self.tail:
            self.tail = None
        else:
            tail.next.prev = head
            self.tail = tail.next
            head.next = self.tail
            
        return tail

    def __iter__(self):
        curr = self.tail

        if curr:
            while curr.next is not self.tail:
                yield curr
                curr = curr.next
            yield curr


class Node:

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)
