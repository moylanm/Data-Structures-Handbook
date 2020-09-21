[Array](array.md) | [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) | __Stack__ | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)

# Stack

A stack is a container of elements that are added (pushed) and removed (popped) according to the Last-In-First-Out (LIFO) principle. Stacks have limited access since elements can only be added to, or removed from, the top of the stack.

The Last-In-First-Out principle states that the last element to be added to the stack will be the first one to be removed.

A stack can be implemented using an array or a linked list. In an array-based implementation the stack will have a maximum capacity of allocated memory, whereas a linked list-based implementation will not.

<br>

# In Memory

In memory, a stack looks like this:

![Stack in memory.](images/stack.png)

In the case of an array-based implementation, the stack, when instantiated, will get the base address of the array from the operating system. When an element is pushed it will be appended to the array using the __(base address + sizeof(datatype) * array.length)__ calculation to assign the new element's memory address. Once the new element has been appended, the stack's ```top``` reference (if it has one) will point to said element.

With a linked list-based implementation, when the stack is instantiated its ```top``` reference will have a ```null``` value. When called upon to push a new element to the stack it will assign the new element's ```next``` attribute to point to the current ```top``` reference (either ```null``` in the case of an empty stack, or the memory address of the current top element). Finally, the stack will change the ```top``` reference to the newly added element.

<br>

# Operations

| Operation | Arguments | Time Complexity | Description |
| --------- | --------- | --------------- | ----------- |
| __Push__ | ```element``` | O(1) | Push a new ```element``` to the top of the stack. When a stack is given a new element to push, it makes that new element the new ```top``` reference. In an array-based implementation it will simply append the new element to the end of the list. In a linked list-based implementation it will make the new element's ```next``` reference point to the previous top element. In both cases the operation happens in constant time.
| __Pop__ | ```None``` | O(1) | Remove and retrieve the top element from the stack. When called upon to execute a __Pop__ operation, a stack will retrieve the current top element, change its ```top``` reference to the next element down, and return the previously retrieved element. Since the stack always keeps track of the top element the time complexity is constant.
| __Peek__ | ```None``` | O(1) | Retrieve the top element from the stack without removing it. In the case of a __Peek__ invocation, the stack will return the top element without removing or changing its ```top``` reference. Like __Pop__, this is also of a constant time complexity.


<br>

# Use Cases

## Advantages

* Stacks are useful when the state of a program needs to be saved. To implement an undo/redo feature in a notepad application, for example, when a user makes a change to the document save its state by pushing it to the top of the stack. The program's state will be that of the top element on the stack. When called upon to undo a change, the program will pop the top element (state) off the stack, making the new top element the currently displayed state.

* When the history of a process needs to be saved a stack is also very useful. Say you want to write a program that finds a way out of a maze. Every step through the maze that the program takes is pushed onto the stack, and when it finds the end of the maze it can return the order of steps it took to find the exit.

* Stacks are also invaluable in programming environments. When a program runs it uses a stack to keep track of which function is currently being executed. The function "below" the top, currently executing, function is it's caller. When the top function is finished executing it will be popped off the stack and return process control to the caller.

## Disadvantages

* Since stacks operate by the Last-In-First-Out principle, the way their data is accessed is limited. The only way to add data is to push it to the top of the stack, and the only data that can be immediately retrieved is by peeking at, or popping from, the top. In order to retrieve the bottom-most element a program would have to pop off every element in the stack until it reached the base.

* Stack instruction sets do not typically handle cases where a program tries to pop from an empty stack, so the program author is responsible for handling such situations.

* Stacks do not inherently support search functionality. Accessing any other element in the stack other than the one on top is not how stacks are meant to work.

* In the case of an array-based implementation, the largest potential size of a given stack needs to be accounted for when allocating memory. This can result in wasted memory space.

<br>

# Demonstration

```python
>>> stk = Stack()
>>> print(stk)
(Base) [] (Top)
>>> stk.pop()
'Stack is empty.'
>>> stk.push(7)
>>> print(stk)
(Base) [7] (Top)
>>> stk.push(9)
>>> stk.push(3)
>>> stk.push(5)
>>> print(stk)
(Base) [7, 9, 3, 5] (Top)
>>> stk.pop()
5
>>> print(stk)
(Base) [7, 9, 3] (Top)
>>> stk.peek()
3
>>> stk.pop()
3
>>> print(stk)
(Base) [7, 9] (Top)
>>> stk.pop()
9
>>> stk.pop()
7
>>> stk.pop()
'Stack is empty.'
>>> print(stk)
(Base) [] (Top)
```

<br>

# Implementation

```python
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

    def __repr__(self):
        return '(Base) {} (Top)'.format(self.stack)

    def __str__(self):
        return '(Base) {} (Top)'.format(self.stack)
```

<br>

(c) 2018 Myles Moylan. All rights reserved.

[Array](array.md) | [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) | __Stack__ | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)
