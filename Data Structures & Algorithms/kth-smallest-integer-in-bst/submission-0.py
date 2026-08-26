# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        maxHeap = [] # limit to size k

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            
            heapq.heappush(maxHeap, -node.val)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

            dfs(node.right)
        
        dfs(root)
        
        return -maxHeap[0]