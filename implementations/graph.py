# coding: utf-8


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
