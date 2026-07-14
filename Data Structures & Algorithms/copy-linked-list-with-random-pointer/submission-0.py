"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new = {}

        def dfs(node):
            if not node:
                return None
            if node in old_new:
                return old_new[node]

            copy = Node(node.val)
            old_new[node] = copy
            copy.next = dfs(node.next)
            copy.random = dfs(node.random)
            return copy
        
        return dfs(head)