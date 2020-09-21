[Array](array.md) | __Tuple__ | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) | [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)

# Tuple

A tuple is a heterogenous, immutable, ordered sequence of data.

<br>

# In Memory

In memory, a tuple looks like this:

![Tuple in memory.](images/tuple.png)

Since tuples are heterogenous, they cannot store elements the same way an array would. Instead, each index is associated with a pionter to its respective element.

Also, being immutable, tuples have no reason to over-allocate memory like an array or list do. Therefore, they only allocate as much memory as they need on instantiation.

<br>

# Operations

| Operation | Arguments | Time Complexity | Description |
| --------- | --------- | --------------- | ----------- |
| __Access__ | ```index``` | O(1) | Retrieve element at given ```index```. Since a tuple utilizes an array structure for storage, accessing via an ```index``` happens in constant time.
| __Search__ | ```item``` | O(n) | Search for a given ```item``` in the tuple. This requires a linear search of the tuple.

<br>

# Use Cases

## Advantages :

* Tuples provide fast, random access to their elements.

* Being immutable can protect data in tuples from being unintentionally, or intentionally, modified. When a sequence of data does not need to be modified it is a good time to use a tuple.

* Immutability also allows for efficient use of memory. A given tuple will only use a certain, static amount of memory throughout its life-cycle.

## Disadvantages :

* Tuple carry pretty significant restraints since they are immutable. If you need to be able to add, remove, or change values of elements in a sequence of data, then tuples are unusable.

<br>

# Demonstration

```python
>>> tup = tuple([1, 'Dog', set(), 42])
>>> tup
(1, 'Dog', set(), 42)
>>> tup[0] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> for item in tup:
...     item
...
1
'Dog'
set()
42
```

<br>

(c) 2018 Myles Moylan. All rights reserved.

[Array](array.md) | __Tuple__ | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) | [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)