"""
Understand

paths[i] = [cityAi, cityBi]

paths = [
["London", "New York"],
["New York", "Lima"],
["Lima", "Sao Paulo"]
]

output = Sao Paulo

Plan

1. Translate the problem into graph terminology
Vertices = Cities
Edges = paths from city to city
Weights = None

2. Build your graph

use an adjacency list
Each key is a City (origin)
values will be it's neighboring city that it has a route to


3. Traverse the graph
BF/DF?

[link](https://leetcode.com/problems/destination-city/)
"""
# from collections import deque

# class Solution:
#     def destCity(self, paths: List[List[str]]) -> str:
#         if len(paths) == 0:
#             return ''
#         graph = self.createGraph(paths)
#         stack = deque()
#         stack.append(paths[0][0])
#         visited = set()
#         while len(stack) > 0:
#             curr = stack.pop()
#             visited.add(curr)
#             if curr not in graph:
#                 return curr
#             else:
#                 for neighbor in graph[curr]:
#                     if neighbor not in visited:
#                         stack.append(neighbor)
#         return ''
        
#     def createGraph(self, paths):
#         graph = {}
#         for edge in paths:
#             origin, destination = edge[0], edge[1]
#             if origin in graph:
#                 graph[origin].add(destination)
#             else:
#                 graph[origin] = { destination }
#         return graph
    