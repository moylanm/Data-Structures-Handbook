[Array](array.md) | [Tuple](tuple.md) | [Dictionary](dictionary.md) | __Set__ | [Linked List](linked_list.md) | [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)

# Set

A set is a heterogenous, unordered collection of immutable data objects which does not allow for  duplicates. Sets utilize hash tables which grants fast, constant time access and storage of data.

<br>

# In Memory

In memory, a set looks like this:

![Set in memory.](images/set.png)

Sets utilize hash tables, not unlike dictionaries. They only difference being that sets do not hold key-value pairs, instead storing single, unique keys. When a key is added it is run through the hash function, resulting in an integer that is within the hash table's possible positions; in index of the hash table's array. The bucket associated with the index is then assigned the original value of the given key.

One bucket of the set holds the hash codes of the stored keys and one holds pointers to the key values themselves. Memory addresses for both buckets and key objects are chosen arbitrarily, and the amount of memory allocated depends on the type of object and its implementation.

In Python a set will start with eight empty buckets, doubling the amount whenever it reaches capacity.

<br>

# Operations

| Operation | Arguments | Time Complexity | Description |
| --------- | --------- | --------------- | ----------- |
| __Access__ | ```item``` | O(1) | Access the given ```item``` within the set. This can also be used to check whether a set contains the given ```item```. Since dictionaries utilize hash tables this operation has O(1) time complexity.
| __Store__ | ```item``` | O(1) | Add a given ```item``` to the set. Since sets utilize hash tables this is a constant time operation.
| __Remove__ | ```item``` | O(1) | Remove a given ```item``` from the set. Since sets utilize hash tables this is a constant time operation.

<br>

# Use Cases

## Advantages :

* Since sets are implemented with hash tables they provide access, storage, and removal operations with O(1) time complexity.

* Set operations like union, intersect, and difference are very useful and simple ways to compare elements of multiple sets.

## Disadvantages :

* There may be times when duplicate elements need to be accounted for, in this case sets cannot be used.

<br>

# Demonstration

```python
>>> s = set()
>>> s
set()
>>> s.add(42)
>>> s.add('Dog')
>>> s.add(1.5)
>>> s
{1.5, 42, 'Dog'}
>>> s.add(42)
>>> s
{1.5, 42, 'Dog'}
>>> s.remove('Dog')
>>> s
{1.5, 42}
>>> 42 in s
True
>>> 'Dog' in s
False
```

<br>

(c) 2018 Myles Moylan. All rights reserved.

[Array](array.md) | [Tuple](tuple.md) | [Dictionary](dictionary.md) | __Set__ | [Linked List](linked_list.md) | [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)