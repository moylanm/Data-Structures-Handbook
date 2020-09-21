[Array](array.md) | [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) | [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | __Graph__

# Graph

A graph is an illustrated representation of a set of objects, or vertices, where some are connected by links, or edges.

Formally, a graph is a pair of sets ```(V, E)``` where ```V``` is the set of vertices and ```E``` is the set of edges. Each vertex has a unique ```key``` or ```id``` to identify it, while each edge may have a ```weight``` to indicate the cost of travelling between two vertices.

Graphs can be implemented in a couple ways, one being via a dictionary or hash table. With a dictionary a ```Vertex``` object can be stored as a value associated with the ```key``` given to it at instantiation. Furthermore, each ```Vertex``` object can hold a dictionary to store references to any adjacent nodes along with the ```weight``` of the edge connecting them. This implementation method allows fast, constant time access, storage, and deletion of vertices and edges within the graph.

<br>

# In Memory

In memory, a graph looks like this:

![Graph in memory.](images/graph.png)

The ```Graph``` class used in this example has a ```vertice_list``` attribute which is a dictionary that holds every vertex within the graph. Each key in the dictionary is set as the ```id``` of the vertex, while the associated value is a reference to the ```Vertex``` object itself. Within each of those objects there is an ```id``` and ```adj``` attribute, where ```id``` is the name of the vertex and ```adj``` is a dictionary holding any neighboring ```Vertex```objects. Within the ```adj``` attribute's dictionary, the key is a reference to the neighboring ```Vertex``` and the associated value is the weight of the connecting edge.

In memory, address locations will be arbitrary. The ```Graph``` instance will have its own address, as will the ```vertice_list```. Within the ```vertice_list```, there will be references to each ```Vertex``` object with its own arbitrarily chosen memory address, along with the dictionary held by the ```adj``` attribute. 

Larger graphs with more vertices will develop larger dictionaries. Once a dictionary reaches capacity it will allocate double the amount of memory it currently utilizes. So the combination of the ```Graph```, its ```vertice_list```, and each member ```Vertex``` with its own dictionary, can certainly add up to a significant amount of memory usage.

<br>

# Operations

| Operation | Arguments | Time Complexity | Description |
| --------- | --------- | --------------- | ----------- |
| __Access__ | ```key``` | O(1) | Access a vertex with given ```key```. Similar to accessing the entry of a set or dictionary, this operation is constant.
| __Store__ | ```key``` | O(1) | Store a vertex with given ```key```. Similar to adding a new item into a set or dictionary, this operation is constant.
| __Delete__ | ```ket``` | O(1) | Delete vertex with given ```key```. Same as removing an item from a set or dictionary, O(1) time complexity.

<br>

# Use Cases

## Advantages :

* Graphs are useful for representing, analyzing, and working with networks. Examples include transportation systems, computer networks, and even molecules in chemistry and physics.

* There are many useful algorithms for analyzing graphs, like Dijkstra's shortest path and Prim's spanning tree algorithms.

## Disadvantages :

* While graphs are invaluable for handling crucial problems, their uses are constrained to those very problems. A graph would not be appropriate for a problem that requires a queue, a stack, a tree, or a linked list. 

<br>

# Demonstration

```python
>>> g = Graph()
>>> for i in range(6):
...     g.add_vertex(i)
...
0
1
2
3
4
5
>>> g.vertice_list
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
>>> g.add_edge(0, 1, 5)
>>> g.add_edge(0, 5, 2)
>>> g.add_edge(1, 2, 4)
>>> g.add_edge(2, 3, 9)
>>> g.add_edge(3, 4, 7)
>>> g.add_edge(3, 5, 3)
>>> g.add_edge(4, 0, 1)
>>> g.add_edge(5, 4, 8)
>>> g.add_edge(5, 2, 1)
>>> g
0 connected to: [1, 5, 4]
neighbor | edge_weight
1          5
5          2
4          1

1 connected to: [0, 2]
neighbor | edge_weight
0          5
2          4

2 connected to: [1, 3, 5]
neighbor | edge_weight
1          4
3          9
5          1

3 connected to: [2, 4, 5]
neighbor | edge_weight
2          9
4          7
5          3

4 connected to: [3, 0, 5]
neighbor | edge_weight
3          7
0          1
5          8

5 connected to: [0, 3, 4, 2]
neighbor | edge_weight
0          2
3          3
4          8
2          1
```

<br>

# Implementation

```python
class Graph:

    def __init__(self):
        self.vertice_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        self.vertice_list[key] = Vertex(key)
        return self.vertice_list[key]

    def get_vertex(self, n):
        return self.vertice_list[n] if n in self.vertice_list else None

    def add_edge(self, vert_key_1, vert_key_2, cost=0):
        if vert_key_1 not in self.vertice_list:
            new_vertex = self.add_vertex(vert_key_1)
        if vert_key_2 not in self.vertice_list:
            new_vertex = self.add_vertex(vert_key_2)
        self.vertice_list[vert_key_1].add_neighbor(self.vertice_list[vert_key_2],
                                                    cost)
        self.vertice_list[vert_key_2].add_neighbor(self.vertice_list[vert_key_1],
                                                    cost)

    def get_vertices(self):
        return self.vertice_list.keys()

    def __contains__(self, n):
        return n in self.vertice_list

    def __iter__(self):
        return iter(self.vertice_list.values())

    def __repr__(self):
        return '\n\n'.join([
                           '{0} connected to: {1}\n{2}\n{3}'
                           .format(vrt, list(vrt.get_connections()), 'neighbor | edge_weight', 
                                '\n'.join([
                                          '{!r: <3}{!r: >9}'
                                          .format(nbr, vrt.get_weight(nbr)) 
                                          for nbr in vrt.get_connections()
                                         ])
                                  )
                           for vrt in self
                          ])


class Vertex:

    def __init__(self, key):
        self.id = key
        self.neighbors = {}

    def add_neighbor(self, nbr, weight=0):
        self.neighbors[nbr] = weight

    def get_connections(self):
        return self.neighbors.keys()

    def get_id(self):
        return self.id
    
    def get_weight(self, nbr):
        return self.neighbors[nbr]

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)
```

<br>

(c) 2018 Myles Moylan. All rights reserved.

[Array](array.md) | [Tuple](tuple.md) | [Dictionary](dictionary.md) | [Set](set.md) | [Linked List](linked_list.md) | [Stack](stack.md) | [Queue](queue.md) | [Tree](tree.md) | __Graph__