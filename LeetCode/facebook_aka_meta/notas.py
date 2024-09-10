 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        nodes = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        minCol, maxCol = 0, 0 
        # BFS better than DFS as we go top to bottom so 
        # nodes in same col at higher row will come first in list 
        # With DFS this many not happen as we can reach node at lower level first 
        while queue:
            for _ in range(len(queue)):
                node, col = queue.popleft()
                nodes[col].append(node.val)
                if node.left:
                    queue.append((node.left, col-1))
                    minCol = min(minCol, col-1)
                if node.right:
                    queue.append((node.right, col+1))
                    maxCol = max(maxCol, col+1)
        ans = []
        # Since we know the min and max col value, we don't have
        # to sort the dict by keys. Also there will always be 
        # a value for all cols between min and max col as we can't 
        # skip a col to get to next col.
        for col in range(minCol, maxCol+1):
            ans.append(nodes[col])
        return ans