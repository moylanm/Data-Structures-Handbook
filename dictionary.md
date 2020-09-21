[Array](array.md) | [Tuple](tuple.md) | __Dictionary__ | [Set](set.md) | [Linked List](linked_list.md) | [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)

# Dictionary

A dictionary is a heterogenous, unordered collection of key/value pairs which does not allow for duplicate keys. Dictionaries utilize hash tables which grants fast, constant time access and storage of data.

<br>

# In Memory

In memory, a dictionary looks like this:

![Dictionary in memory.](images/dictionary.png)

Dictionaries utilize hash tables in order to store their key-value pairs. A hash function will take a key as input and perform a calculation that results in an integer that is within the range of the hash table's possible positions; essentially an index of the hash table's array. Buckets, or slots, associated with the resulting index of the has table are then made to hold both the original key and accompanying value.

Three separate buckets are used by Python dictionaries: one holds hash codes of the stored keys, one holds the pointers to key values themselves, and one holds the pointers to values associated with those keys. Each bucket, key, and value will have its own arbitrarily chosen memory address. The amount of memory allocated for each object depends on its size and implementation.

In Python a dictionary will start with eight empty buckets, doubling the amount whenever it reaches capacity.

<br>

# Operations

| Operation | Arguments | Time Complexity | Description |
| --------- | --------- | --------------- | ----------- |
| __Access__ | ```key``` | O(1) | Access the ```value``` of a given ```key```. This can also be used to check whether a dictionary contains the given ```key```. Since dictionaries utilize hash tables this operation has O(1) time complexity.
| __Store__ | ```key```, ```value``` | O(1) | Store a ```key``` with given ```value```. Since dictionaries utilize hash tables this operation has O(1) time complexity.
| __Remove__ | ```key``` | O(1) | Remove given ```key``` from dictionary. Since dictionaries utilize hash tables this operation has O(1) time complexity.

<br>

# Use Cases

## Advantages :

* When a program is handling some sort of meaningful key-value relationship mapping, then a dictionary should be considered.

* Since dictionaries use hash tables, they grant lookup operations at O(1) time.

## Disadvantages :

* Dictionaries use hash tables, so there is always potential for key collisions.

* The ordering of dictionary elements is arbitrary, it can change on a case-by-case bases. 

<br>

# Demonstration

```python
>>> d = dict()
>>> d
{}
>>> d[18] = 'Giraffe'
>>> d[1] = 42
>>> d
{18: 'Giraffe', 1: 42}
>>> d['Black'] = 'White'
>>> d
{18: 'Giraffe', 1: 42, 'Black': 'White'}
>>> del d[1]
>>> d
{18: 'Giraffe', 'Black': 'White'}
>>> 1 in d
False
>>> 18 in d
True
```

<br>

(c) 2018 Myles Moylan. All rights reserved.

[Array](array.md) | [Tuple](tuple.md) | __Dictionary__ | [Set](set.md) | [Linked List](linked_list.md) | [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | [Graph](graph.md)