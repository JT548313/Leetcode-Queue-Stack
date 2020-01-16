# Definition for a Node.
import copy


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None

        visited = {}

        def dfs(cur_node: 'Node') -> 'Node':
            if cur_node in visited:
                return visited[cur_node]

            new_node = Node(cur_node.val, [])
            visited[cur_node] = new_node
            for neigh in cur_node.neighbors:
                new_node.neighbors.append(dfs(neigh))
            return new_node

        return dfs(node)




