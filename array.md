__Array__ | [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) |  [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)

# Array

An array is a homogenous, ordered, contiguous collection of elements with each element identified by an index. Since array implementations utilize the size of the data type being stored, the elements of an array are typically required to be of the same size and of the same type (homogenous).

<br>

# In Memory

In memory, an array looks like this:

![Array in memory.](images/array.png)

When an array is instantiated it gets its base memory address (likely from the operating system). When an element is appended, the array implementation calculates the next available space using the (stored) value of its current length. 

## For Example :

If an array is empty and is called upon to append an integer, then the memory address calculation will happen like so:

Where:

* Base Address = 0x1000
* Array Length = 0
* Datatype Size = 24 bytes (0x18)

Calculate the memory address at the end of the array via __(base address + sizeof(int) * array.length)__ and place the new element there. Once that is complete, increment the length of the array.

__(base address + sizeof(int) * array.length)__ = __(0x1000 + 0x18 * 0x0)__ = __0x1000__

So the new element would be inserted at the base of the array, at memory address 0x1000.

---

Now say the array is holding 4 integers. If it were called upon to append another element the calculation would go like so:

Where:

* Base Address = 0x1000
* Array Length = 4
* Datatype Size = 24 bytes (0x18)

Again, calculate the memory address at the end of the array and insert the new integer at that location. Finally, increment the length of the array.

__(base address + sizeof(int) * array.length)__ = __(0x1000 + 0x18 * 0x4)__ = __0x1060__

So the new element would be inserted at the 4th index of the array, at memory address 0x1060.

<br>

# Operations

| Operation | Arguments | Time Complexity | Description |
| --------- | --------- | --------------- | ----------- |
| __Access__ | ```index``` | O(1) | Retrieve (access) a value stored at a specified available ```index```. An array keeps on hand the memory address of the base of the array and the size of the datatypes it is holding. Given the index of an element, the memory address can be calculated in constant time via: __(base address + sizeof(datatype) * index)__.
| __Append__ | ```value``` | O(1) | Add a ```value``` to the end of the array. An array keeps track of the last occupied index (or the length of the array). When it appends a new value, it simply adds the value to the end of the array using the same calculation method (in constant time) as when it accesses values: __(base address + sizeof(datatype) * array.length)__.
| __Update__ | ```index```, ```value``` | O(1) | Update an element at a specified available ```index``` with a new ```value```. When updating an element, an array will calculate the memory address of the given index and replace the old value with the new one. This operation (like __Access__) happens in constant time.
| __Insert__ | ```index```, ```value``` | O(n) | Insert a ```value``` at a specified available ```index```. When inserting a value at a specified index, before doing so the array must shift all the elements coming after the index one space away from the base of the array. One this is done the new value can be inserted without losing the data that used to occupy said index. The shifting of elements happens in linear time.
| __Delete__ | ```value``` | O(n) | Delete a given ```value```. When an array deletes an element it shifts those elements after it one space toward the base of the array. The shifting of elements happens in linear time.
| __Search__ | ```value``` | O(n) | Search the array for a given ```value```. Using a basic search implementation, the search function will start at one end of the array and continue up or down until it either finds the value or reaches the other end. This search method results in linear time complexity. Using a method like a binary search has a better chance of yielding results quicker, having a time complexity of O(log n).

<br>

# Use Cases

## Advantages

* The array is one of the most efficient data structures for storing and accessing a sequence of elements. Arrays allow random access of elements. This means that one can access any desired element independently, and in constant time, of what other elements have been or will be accessed.

* If a there is a job that needs to store large amounts of data and requires quick access, then an array is most likely best suited for the task.

* Arrays are also invaluable when implementing other data structures like linked lists, stacks, queues, trees, and graphs.


## Disadvantages

* One must know in advance how many elements are to be stored in an array. An array is a static structure, which means that the amount of memory allocated for it is fixed. If an array reaches the end of its granted memory, it must allocate an entirely separate block and copy every element within the old memory space to the new one; this can come at a substantial cost of time.

* Since an array is of a fixed size, programs that allocate memory for them tend to allocate more than is needed. However, if not enough memory is allocated then the problem of reallocating and copying data arises.

* Since the elements of an array are stored contiguously, insertion and deletion tend to be difficult and time consuming.

<br>

# Demonstration

```python
>>> arr = Array()
>>> print(arr)
[]
>>> arr[1]
'Index out of range.'
>>> arr.append(2)
>>> print(arr)
[2]
>>> arr.append(4)
>>> print(arr)
[2, 4]
>>> arr.insert(1, 5)
>>> print(arr)
[2, 5, 4]
>>> arr.search(5)
1
>>> arr.search(4)
2
>>> arr.search(6)
'Value not found.'
>>> arr.delete(2)
>>> print(arr)
[5, 4]
```

<br>

# Implementation

```python
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
```

<br>

(c) 2018 Myles Moylan. All rights reserved.

__Array__ | [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) |  [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)
