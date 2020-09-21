[Array](array.md) | [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) | [Stack](stack.md) | __Queue__ | [Tree](tree.md) | [Graph](graph.md)

# Queue

A queue is a heterogenous, ordered sequence of data that operates in accordance with the First-In-First-Out (FIFO) principle. The first element added is the first to be removed. Unlike stacks, queues are open at both ends. In the case of a queue, one end is for queueing (back) and one for dequeueing (front). And in the case of a deque, each end supports both enqueueing and dequeueing.

<br>

# In Memory

In memory, a queue looks like this:

![Queue in memory.](images/queue.png)

Queues can be implemented using arrays and linked lists. Array-based implementations are not as efficient as those implementing linked lists, both in terms of the amount of memory used and the time complexity of operations.

Array-based implementations will over-allocate memory in anticipation of the addition of new elements. Also, when enqueueing or dequeueing to or from the base index, every element must be shifted either up or down the array to accommodate for the change (a linear time operation).

Linked list-based queues only use up as much memory as they have items. Granted, the memory space a given item takes up may very well be more than that of an array's element. However, when it comes to the time complexity of enqueueing and dequeueing, linked lists come out on top. As long as the queue's linked list holds pointers to the ```front``` and ```back``` nodes, enqueueing and dequeueing is a constant time operation; this can also be accomplished with a circularly-linked list.

<br>

# Operations

| Operation | Arguments | Time Complexity | Description |
| --------- | --------- | --------------- | ----------- |
| __Enqueue__ | ```item``` | O(1) | Enqueue a given ```item``` to the front (queue), or either end (deque), of the queue. Similar to the push operation of a stack, __Enqueue__ adds a given element to an end of the queue; in constant time.
| __Dequeue__ | ```None``` | O(1) | Dequeue the element from the back (queue), or either end (deque), of the queue. A queue essentially pops the element from an end and returns it to the caller; in constant time.
| __Peek__ | ```None``` | O(1) | Retrieve the element at the front (queue), or either end (deque), of the queue without dequeueing. In this case the queue will return a reference to the front or back element without removing it; in constant time.

<br>

# Use Cases

## Advantages

* Queues are useful when, for example, there are multiple users trying to access a given resource. When each user requests the resource in question, each request will be enqueued and handled in the order received. This ensures that the wait time for each request to be answered is as short as possible.

* Adding and removing elements from a queue, or deque, happens in constant time when implemented properly.

* Queues can handle virtually any data types; providing more flexibility than, for example, an array.

* Priority queues are different than the classical queues in that instead of operating according to the First-In-First-Out principle, they dequeue elements according to their priority. Use cases include CPU scheduling and graph traversal algorithms, like Dijkstra's shortest-path algorithm or Prim's algorithm.

## Disadvantages

* Queues are not readily searchable. Whether implemented using an array or a linked list, searching for a given element in a queue would require an O(n) operation. Granted, there are probably ways around this, but the point is that they do not inherently support searching.

* Deleting elements within a queue that are not occupying the front or rear can prove to be complex problems. Not only would an implementation have to search through the queue, but when it finds the desired element the operation used to delete that element changes depending on how the queue is implemented.

<br>

# Demonstration

### Queue
```python
>>> q = Queue()
>>> print(q)
(Back)  (Front)
>>> q.dequeue()
>>> q.enqueue(7)
>>> q.enqueue(21)
>>> q.enqueue('Giraffe')
>>> print(q)
(Back) Giraffe 21 7 (Front)
>>> q.dequeue()
7
>>> print(q)
(Back) Giraffe 21 (Front)
>>> q.enqueue(list())
>>> q.enqueue(42)
>>> print(q)
(Back) 42 [] Giraffe 21 (Front)
>>> q.dequeue()
21
>>> q.peek()
Giraffe
>>> q.dequeue()
Giraffe
>>> q.dequeue()
[]
>>> q.peek()
42
>>> print(q)
(Back) 42 (Front)
```

### Deque
```python
>>> dq = Deque()
>>> print(dq)
(Back)  (Front)
>>> dq.dequeue_front()
>>> dq.dequeue_rear()
>>> dq.enqueue_front(12)
>>> dq.enqueue_front(set())
>>> print(dq)
(Back) 12 set() (Front)
>>> dq.enqueue_front('Dog')
>>> dq.enqueue_rear('Chicken')
>>> print(dq)
(Back) Chicken 12 set() Dog (Front)
>>> dq.dequeue_rear()
Chicken
>>> dq.peek_rear()
12
>>> print(dq)
(Back) 12 set() Dog (Front)
>>> dq.dequeue_front()
Dog
>>> dq.peek_front()
set()
>>> dq.dequeue_front()
set()
>>> print(dq)
(Back) 12 (Front)
```

<br>

# Implementation

```python
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
```

<br>

(c) 2018 Myles Moylan. All rights reserved.

[Array](array.md) | [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) | [Stack](stack.md) | __Queue__ | [Tree](tree.md) | [Graph](graph.md)