"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        try:
            self.vertices[vertex_id]
        except KeyError:
            self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        found = set()
        vertex_queue = Queue()
        
        found.add(starting_vertex)
        vertex_queue.enqueue(starting_vertex)

        while vertex_queue.size() > 0:
            current_vertex = vertex_queue.dequeue()
            print(current_vertex)
            neighbors = self.get_neighbors(current_vertex)
            for vertex in neighbors:
                if vertex not in found:
                    found.add(vertex)
                    vertex_queue.enqueue(vertex)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        found = set()
        vertex_stack = Stack()

        found.add(starting_vertex)
        vertex_stack.push(starting_vertex)

        while vertex_stack.size() > 0:
            current_vertex = vertex_stack.pop()
            print(current_vertex)
            neighbors = self.get_neighbors(current_vertex)
            for vertex in neighbors:
                if vertex not in found:
                    found.add(vertex)
                    vertex_stack.push(vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        found = set()
        found.add(starting_vertex)

        self.__dft_recursive(starting_vertex, found)

    
    def __dft_recursive(self, current_vertex, found):
        print(current_vertex)

        neighbors = self.get_neighbors(current_vertex)

        for vertex in neighbors:
            if vertex not in found:
                found.add(vertex)
                self.__dft_recursive(vertex, found)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        found = set()
        vertex_queue = Queue()

        found.add(starting_vertex)
        vertex_queue.enqueue( (starting_vertex, [starting_vertex]) )

        while vertex_queue.size() > 0:
            current_vertex, vertex_path = vertex_queue.dequeue()

            if current_vertex == destination_vertex:
                return vertex_path
            else:
                neighbors = self.get_neighbors(current_vertex)

                for vertex in neighbors:
                    vertex_queue.enqueue( (vertex, vertex_path + [vertex]) )


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        found = set()
        vertex_stack = Stack()

        found.add(starting_vertex)
        vertex_stack.push( (starting_vertex, [starting_vertex]) )

        while vertex_stack.size() > 0:
            current_vertex, vertex_path = vertex_stack.pop()
            found.add(current_vertex)

            if current_vertex == destination_vertex:
                return vertex_path
            else:
                neighbors = self.get_neighbors(current_vertex)

                for vertex in neighbors:
                    if vertex not in found:
                        vertex_stack.push( (vertex, vertex_path + [vertex]) )


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        found = set()
        found.add(starting_vertex)

        return self.__dfs_recursive(starting_vertex,destination_vertex, found, [starting_vertex])

    
    def __dfs_recursive(self, current_vertex, destination_vertex, found, current_path):
        neighbors = self.get_neighbors(current_vertex)
        found.add(current_vertex)

        if current_vertex == destination_vertex:
            return current_path
        else:
            end_of_path = True
            for vertex in neighbors:
                if vertex not in found:
                    end_of_path = False
                    result = self.__dfs_recursive(vertex, destination_vertex, found, current_path + [vertex])

                    if result is not None:
                        return result

            if end_of_path:
                return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
