[Array](array.md) | [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) | [Stack](stack.md) | [Queue](queue.md) | __Tree__ | [Graph](graph.md)

# Tree

A tree is a hierarchical collection of data with a root node and subtrees of children nodes. Every node in a tree, except for the root node, has a parent node.

<br>

# In Memory

In memory, a tree looks like this:

![Tree in memory.](images/tree.png)

The memory footprint of a tree depends on how it is implemented. Different types of trees require different implementations. Each tree works under different constraints, follows different rules, and consists of different operations.

Above, I have a BinarySearchTree class implemented using a TreeNode class to represent each node in the tree. The TreeNode class has four attributes: a ```key``` which holds a reference to the name or value associated with the node, a reference to the node's ```parent```, and references to the node's ```left_child``` and ```right_child```. The memory addresses for the BinarySearchTree class, along with those of any TreeNodes within the tree, are arbitrarily chosen. Because of the over-allocation of the BinaryMinHeap's array, the BinarySearchTree has potential to have the upper hand when it comes to efficient memory usage.

The BinaryMinHeap class, because if the way it operates, is able to use a simple array to hold all of its node data. The ```heap_list``` array is initialized with a zero, which is ignored, for the purpose of integer division. A binary heap uses division and multiplication to traverse up and down, respectively, the nodes in the tree. The calculations it uses are:

* ```parent_index``` = ```node_index``` // 2
* ```left_child_index``` = ```node_index``` * 2
* ```right_child_index``` = ```node_index``` * 2 + 1

With the property of random access, the BinaryMinHeap has the potential to traverse and modify the tree quickly. There are, however, the drawbacks of over-allocation and upper limit of available memory. 

<br>

# Operations

| Operation | Arguments | Time Complexity | Description |
| --------- | --------- | --------------- | ----------- |
| __Access__ | ```key``` | O(log n) | Access a node with a given ```key```. To access a node it first needs to be found, requiring a search which performs at O(log n).
| __Insert__ | ```key``` | O(log n) | Insert a new node with a given ```key```. To insert a new node into the tree is a constant operation. However, once a new node is inserted the tree will move it to its proper place, an operation with a time complexity of O(log n).
| __Delete__ | ```key``` | O(log n) | Delete a node with a given ```key```. To access a node it first needs to be found, requiring a search which performs at O(log n). 
| __Search__ | ```key``` | O(log n) | Search for a node with a given ```key```. For a tree to search for a given node it will typically start at the ```root``` node and traverse down from there until it finds the node it's looking for or reaches the bottom; a logarithmic operation.

<br>

# Use Cases

## Advantages :

* Trees are useful for storing information that naturally forms a hierarchy, like the file system of a computer.

* Compared to linear data structures, like arrays or linked lists, trees perform better when searching. When searching, a linked list will perform at O(n) while a tree will perform at O(log n).

## Disadvantages :

* Binary search trees can degrade into a linear sequence of data which results in the time complexity of the __Search__ functionality going from logarithmic to linear.

* Compared to data structures that utilize hash tables, like sets and dictionaries, the search time for trees is slower. Searching with trees performs at O(log n) while searching with sets or dictionaries performs at O(1).

<br>

# Demonstration

### BinarySearchTree
```python
>>> bst = BinarySearchTree()
>>> bst.draw_tree()
1 : []

>>> bst.insert(3)
>>> bst.insert(2)
>>> bst.insert(4)
>>> bst.draw_tree()
1 : [3]
2 : [2] [4]

>>> bst.insert(1)
>>> bst.insert(7)
>>> bst.insert(5)
>>> bst.insert(8)
>>> bst.draw_tree()
1 : [3]
2 : [2] [4]
3 : [1, ' '] [' ', 7]
4 : [' ', ' ', ' ', ' '] [' ', ' ', 5, 8]
```

### BinaryMinHeap
```python
>>> min_heap = BinaryMinHeap()
>>> min_heap
(Root) []
>>> min_heap.insert(4)
>>> min_heap.insert(1)
>>> min_heap.insert(2)
>>> min_heap
(Root) [1, 4, 2]
>>> min_heap.insert(3)
>>> min_heap
(Root) [1, 3, 2, 4]
```

<br>

# Implementation

```python
from collections import namedtuple


class BinarySearchTree:

    def __init__(self, *keys):
        self.root = None
        self.height = 0

        if keys:
            self.insert(*keys)

    def find(self, key):
        node = self.root

        while node and node.key != key:
            if node.key < key:
                node = node.right_child
            else:
                node = node.left_child
        return node

    def insert(self, *keys):
        if not self.root:
            self.root = TreeNode(keys[0])
            self.height = 1
            keys = keys[1:]

        for key in keys:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key == node.key:
            return

        if key < node.key:
            if node.has_left_child():
                self._insert(key, node.left_child)
            else:
                node.left_child = TreeNode(key, node.level + 1, parent=node)
        if key > node.key:
            if node.has_right_child():
                self._insert(key, node.right_child)
            else:
                node.right_child = TreeNode(key, node.level + 1, parent=node)
        
        if node.level + 1 > self.height:
            self.height = node.level + 1

    def delete(self, key):
        node_to_delete = self.find(key)

        if node_to_delete:
            self._delete(node_to_delete)
        else:
            raise KeyError('Key not in tree.')

    def _delete(self, node):
        if node.is_leaf():
            if node.is_root():
                self.root = None
            else:
                setattr(node.parent, node.get_node_side(), None)
        elif node.has_one_child():
            child = node.get_only_child()

            for child in preorder(child):
                child.level -= 1

            if node.is_root():
                child.parent = None
                self.root = child
            else:
                child.parent = node.parent
                setattr(node.parent, node.get_node_side(), child)
        else:
            succ = self.find_min(node.right_child)

            for child in preorder(succ.right_child):
                child.level -= 1

            setattr(succ.parent, succ.get_node_side(), 
                None if succ.is_leaf() else succ.right_child)

            succ.level = node.level
            succ.left_child = node.left_child
            succ.right_child = node.right_child
            node.right_child.parent = succ
            node.left_child.parent = succ

            if node.is_root():
                succ.parent = None
                self.root = succ
            else:
                succ.parent = node.parent
                setattr(node.parent, node.get_node_side(), succ)

        self._verify_height()

    def _verify_height(self):
        self.height = max(node.level for node in preorder(self.root)) \
            if self.root else 0

    def find_min(self, node):
        return self.find_min(node.left_child) if node.has_left_child() else node

    def draw_tree(self):
        if not self.root:
            print('{} : {}'.format(1, []))
            print()
            return

        levels = [level for level in self._bft(self.root)]

        print('{} : {}'.format(levels[0].value, levels[0].keys))
        for level in levels[1:]:
            print(level.value, end=' : ')
            print(level.keys[:len(level.keys) // 2], end=' ')
            print(level.keys[len(level.keys) // 2:])
        
        print()

    def _bft(self, root_node):

        level = namedtuple('Level', ['value', 'keys'])
        yield level(value = root_node.level, keys = [root_node.key])
        
        curr_level = root_node.level + 1
        high_nodes = [root_node]

        while curr_level <= self.height:
            low_nodes = []

            for node in high_nodes:
                if node:
                    low_nodes.extend([node.left_child, node.right_child])
                else:
                    low_nodes.extend([None] * 2)

            yield level(value = curr_level, keys = [node.key if node else ' ' for node in low_nodes])
            high_nodes = low_nodes
            curr_level += 1


class BinaryMinHeap:
    
    def __init__(self):
        self.heap_list = [0]    # initialize with 0 for integer division in other methods
        self.current_size = 0

    def insert(self, key):
        self.heap_list.append(key)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_up(self, index):
        if self.heap_list[index] < self.heap_list[index // 2]:
            self.heap_list[index], self.heap_list[index // 2] = \
                self.heap_list[index // 2], self.heap_list[index]
                
            if index // 2 > 0:
                self.perc_up(index // 2)
    
    def perc_down(self, index):
        if (index * 2) <= self.current_size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                self.heap_list[index], self.heap_list[mc] = \
                    self.heap_list[mc], self.heap_list[index]
                
                self.perc_down(mc)

    def min_child(self, index):
        if index * 2 + 1 > self.current_size or \
            self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
            return index * 2
        else:
            return index * 2 + 1

    def del_min(self, index):
        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list.pop()
        self.current_size -= 1
        self.perc_down(1)
        return root

    def build_heap(self, list_):
        i = len(list_) // 2
        self.current_size = len(list_)
        self.heap_list = [0] + list_
        while i > 0:
            self.perc_down(i)
            i -= 1

    def __repr__(self):
        return '(Root) {}'.format(self.heap_list[1:])

    def __str__(self):
        return '(Root) {}'.format(self.heap_list[1:])


class TreeNode:

    def __init__(self, key, level=1, parent=None, left_child=None, right_child=None):
        self.key = key
        self.level = level
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_one_child(self):
        return bool(self.left_child) ^ bool(self.right_child)

    def has_both_children(self):
        return self.left_child and self.right_child

    def get_only_child(self):
        if self.has_one_child():
            return self.left_child if self.left_child else self.right_child
        return None

    def get_node_side(self):
        if self.is_root():
            return None
        return 'left_child' if self.is_left_child() else 'right_child'


def preorder(node):
    if node:
        yield node
        yield from preorder(node.left_child)
        yield from preorder(node.right_child)

```

<br>

(c) 2018 Myles Moylan. All rights reserved.

[Array](array.md) | [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) | [Stack](stack.md) | [Queue](queue.md) | __Tree__ | [Graph](graph.md)