[Array](array.md)| [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | __Linked List__  | [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)

# Linked List

A linked list is a linear data structure in which the elements are not stored contiguously in memory, but are instead stored in arbitrarily chosen locations in memory. Elements, or nodes, in a linked list hold a piece of data and are linked together by storing pointers to their respective neighbors. There are singly-linked lists, doubly-linked lists, and circular-linked lists.

Nodes in a singly-linked list only store one reference each which points to the next node down the list, whereas nodes in a doubly-linked list store references to both the next and previous nodes.

<br>

# In Memory

In memory, a linked list looks like this:

![Linked List in memory.](images/linked_list.png)

The nodes of a linked-list have their memory addresses arbitrarily chosen when they are instantiated.

In a singly-linked list, each node has two attributes: ```data``` and ```next```. The ```data``` attribute holds a pointer to the node's data object, while ```next``` holds a pointer to the next node down the list. The last node down the list, the ```tail```, has a ```next``` value of ```Null```.

In a doubly-linked list, each node has three attributes: ```data``` (holds a pointer to the node's data object), ```next``` (holds a pointer to the next node down the list), and ```prev``` (holds a pointer to the next node up the list). Both the ```head``` and ```tail``` nodes have ```prev``` and ```next``` values of ```Null```, respectively.

The only difference between a doubly-linked list and a circularly-linked list is that the ```head``` and ```tail``` of a circularly-linked list hold pointers to each other, while those of a doubly-linked list hold ```Null``` values.

<br>

# Operations

| Operation | Arguments | Time Complexity | Description |
| --------- | --------- | --------------- | ----------- |
| __Append__ | ```item``` | O(1) | Append an ```item``` to the head of the list. Since a linked list keeps track of the head element, an append operation will simply create a new node object, instantiated with the new ```item```. It will then assign its ```next``` attribute to reference that of the current ```head```, assign ```previous``` a ```None``` value in the case of a doubly-linked list, and reassign the ```head``` to the newly appended node; all in constant time.
| __Access__ | ```pos``` | O(n) | Access a node at available ```pos```, or index. There is only one point of entry to a linked list, via the ```head``` attribute. Therefore, in order to access a node at a given position the implementation has to iterate starting from the ```head``` until it finds the position it's looking for. So, this happens in linear time.
| __Insert__ | ```pos```, ```item``` | O(n) | Insert a new node with ```item``` at specified, available ```pos```, or index. A linked list will start at the ```head``` and work its way down until it reaches the desired ```pos```. Then it will create a new node with the given ```item```, change the neighboring nodes' references to point to itself, and assigning its own references accordingly; effectively inserting the new node into the list. Since it has to reach the given ```pos``` by iterating over the list, this operation has a linear time complexity.
| __Delete__ | ```item``` | O(n) | Delete a specified ```item``` from the list. After iterating over the list and finding the desired ```item```, the linked list will effectively delete the target node by reassigning the references of its neighboring nodes. Since the list has to search for the given ```item```, __Delete__ happens in linear time.
| __Search__ | ```item``` | O(n) | Search for a specified ```item``` in the list. Starting at the ```head```, a linked list will iterate over each node until it either finds the given ```item``` or reaches the last node. This is a linear time operation. 

<br>

# Use Cases

## Advantages

* Linked lists are dynamic data structures that can grow or shrink at runtime. Since each node of the list is a separate object with an arbitrarily chosen memory address, there is no need for allocating memory like one would with an array.

* Insertion and deletion come at a relatively low cost. instead of having to shift elements one way or another, the references of neighboring nodes are accordingly reassigned to accommodate whichever operation is being executed.

* Linked lists utilize memory efficiently. Instead of allocating a large chunk of memory on instantiation, like an array, a linked list only takes up as much memory as it has nodes.

* Linked lists are useful for implementing other data structures like stacks and queues. Not only do they provide efficient memory utilization, but they also allow for queues to implement queue/dequeue methods that work in constant time.

## Disadvantages

* Traversing a linked list can be costly since there is only one entry point to a given list, the ```head```. In order to reach any node that is not the at the ```head```, the implementation needs to effectively iterate over the list until it finds the desired node; resulting in linear time complexity.

* More memory is used to store a node in a linked list compared to storing an element in an array. Each node holds at least two pieces of data, the ```next``` and ```data``` attributes, and ```prev``` attribute in the case of doubly-linked lists.

* Since, in order to access a given node, traversal is required, random access is not a function of linked lists.

<br>

# Demonstration

### Singly-Linked List
```python
>>> sll = SinglyLinkedList()
>>> print(sll)
(Head) > None
>>> sll.access(2)
'pos parameter not within bounds of list.'
>>> sll.append('Dog')
>>> sll.append('Cat')
>>> print(sll)
(Head) Cat > Dog > None
>>> sll.insert(1, 'Elephant')
>>> sll.insert(2, 42)
>>> print(sll)
(Head) Cat > Elephant > 42 > Dog > None
>>> sll.delete(24)
'Item not found.'
>>> sll.delete('Elephant')
>>> print(sll)
(Head) Cat > 42 > Dog > None
>>> sll.access(1)
42
>>> sll.delete('Dog')
>>> sll.delete('Cat')
>>> print(sll)
(Head) 42 > None
```

### Doubly-Linked List
```python
>>> dll = DoublyLinkedList()
>>> print(dll)
(Head) > None
>>> dll.access(2)
'pos parameter not within bounds of list.'
>>> dll.append('Dog')
>>> dll.append('Cat')
>>> print(dll)
(Head) Cat < > Dog > None
>>> dll.insert(1, 'Elephant')
>>> dll.insert(2, 42)
>>> print(dll)
(Head) Cat < > Elephant < > 42 < > Dog > None
>>> dll.delete(24)
'Item not found.'
>>> dll.delete('Elephant')
>>> print(dll)
(Head) Cat < > 42 < > Dog > None
>>> dll.access(1)
42
>>> dll.delete('Dog')
>>> dll.delete('Cat')
>>> print(dll)
(Head) 42 > None
```

<br>

# Implementation

```python
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
```

<br>

(c) 2018 Myles Moylan. All rights reserved.

[Array](array.md)| [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | __Linked List__  | [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)