Graphs are collections of data represented by nodes and connections between nodes.

Trees can be considered a type of Graphs.

    Formal method of representing networks, or collections of interconnected objects.

    In Mathmatics, Graphs are defined as ordered pairs with two parts: Vertices and Edges.

    Ordered Pair:
        G = (V,E) {
            V = Nodes(Vertices)
            E = Edges or Links. 
            }
    
    Ordered pair is a pair of mathmatical objects in which the order of objects in the pair matters.

    

Components:
    nodes or vertices
        represents objects in a data set (animals, webpages, cities, etc)

    Edges
        connections between vertices; can be bidirectional

        Edges can connect nodes in Any possible way. No rules to how it connects.

            Directed edge: There is only a path from A, the origin, to B, the Destination.
                Example: A website that requires a log-in will log you in and reach you to your destination on completed log-in and won't require a new log-in until logged-out or timed out.

            Undirected Edge: The path between A and B is bidirectional, meaning origin and destination are not fixed.
                Example: A website that has access to each page, linking them.

        Dense
            Contains close to the maximum edges possible

        Sparse
            Contains close to the minimum edges possible

    Weight
        cost to travel across an edge

vertices: (the nodes)
    V = {V0, V1, V2, V3, V4, V5}
Edges: (node 1 - > node 2, cost to travel(optional))
    E = {(v0, v1, 5), (v1, v2, 4), (v2, v3, 9), (v3, v4, 7), (v4, v0, 1), (v0, v5, 2), (v5, v4, 8), (v3, v5, 3), (v5, v2, 1) } 

Useful for:
    Maps - A city/location. Possible stops based on Nodes. Trains you can take to each (edges). Weight (how long it takes)
        Use that information to judge what the best route to take.

    Networks of activity - Git history - Push, pull, etc.

    Any sort of Network
        Social, Physical, etc.



Weighted Graphs:
    Directed Graph - Can only move in one direction along the edges.

    Undirected Graph - can move in both directions along edges (bidirectional).
        There is no Hierarchy of nodes unlike Trees in an Unordered Graph.

Unweighted:
    Cyclic graph = edges allow you to revisit at least one vert.

Acyclic graph = vertices can only be visited once

Relational Data and Representing different data structures/networks.

[link](https://medium.com/basecs/a-gentle-introduction-to-graph-theory-77969829ead8)

[link](http://freefeast.info/difference-between/difference-between-trees-and-graphs-trees-vs-graphs/)

[link](http://stackoverflow.com/questions/7423401/whats-the-difference-between-the-data-structure-tree-and-graph)

[link](http://www.cs.xu.edu/csci390/12s/IJEST10-02-09-124.pdf)

[link](http://www.cs.jhu.edu/~cohen/CS226/Lectures/GraphTraversal.pdf)

[link](https://www.youtube.com/watch?v=gXgEDyodOJU&t=319s)

______________________________________________________________________________________________________________________________________________________

Example of building a Graph Class:


class Graph:
    def __init__(self):
        self.vertices = {
            "A": {"B"},
            "B": {"C", "D"},
            "C": {"E"},
            "D": {"F", "G"},
            "E": {"C"},
            "F": {"C"},
            "G": {"A", "F"}
        }
Adjecency List doesn't use Lists: Vertices collection is a Dict, O(1) constant time.
Edges contained in a set. Check for the existence of edges in O(1).

class Graph:
    def __init__(self):
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,1,1,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,0,0,1,1],
                      [0,0,1,0,0,0,0],
                      [0,0,1,0,0,0,0],
                      [1,0,0,0,0,1,0]]

Matrix as a two-dimensional array = list of lists. Looking at you, Hashtables.


Adjency list runtime/space complexities
v = vertices/nodes

Space: O(v^2)
Add Vertex: O(1)
Remove Verted: O(v)
Add edge: O(1)
Remove ege: O(1)
find edge: O(1)
get all edges: O(1)

Adjacency Matrix:

    Use a matrix to represent whether or not there exists an edge between two vertices

    Matrix[i][j] is True if there exists an edge from vertex i to vertex j

Adjacency Matrix runtime/space complexity
v = vertices/nodes

Space: O(v^2)
    even in a sparse graph, but good for dence graphs because lists are space efficient
Add Vertex: O(v^2)
Remove Vertex: O(v^2)
Add Edge: O(1)
Remove Edge: O(1)
Find Edge: O(1)
Get all edges: O(v)

Graph Traversals

    There are two primary ways to traverse a graph: Depth-first and Breadth-first

    Travel vs. Search
        In a search, you stop once you finf the node you're searching for
        in a traversal, you traverse the entire graph

    Depth-First
        Traverse the graph

        Iterative Psuedocode: To be nameded as DFT_iterative:

        `procedure DFS_iterative(G, v) is
            let S be a stack
            S.push(v)
            while S is not empty do
                v = S.pop()
                if v is not labeled as discovered then
                    label v as discovered
                    for all edges from v to w in G.adjacentEdges(v) do
                        S.push(w)`

        depth-First Traversal Recursive Pseudocode: DFT_Recursive
            `procedure DFS(G, v) is
                label v as discovered
                for all directed edges from v to w that are in G.adjacentEdges(v) do
                    if vertex w is not labeled as discovered then
                        recursively call DFS(G, w)`

    Bredth-First

        Traverse the graph in a breadth-ward motion using a queue
        Very useful for finding the shortest path from node to node

        