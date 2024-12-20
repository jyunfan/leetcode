from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        pass

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # tree to array
        q = deque()
        q.append(root)
        array = []
        while q:
            node = q.popleft()
            array.append(node.val)
            if node.left:
                q.append(node.left)
                q.append(node.right)

        # index
        #0
        #1 2 (2^1-1)
        #3 4 5 6 (2^2-1)
        #7 8 9 10 11 12 13 14 (2^3-1)

        # reverse odd level
        n = len(array)
        for level in range(1, n, 2):
            left = 2 ** level - 1
            right = left + 2 ** level - 1
            
            if left >= n:
                break
            array[left:right+1] = array[left:right+1][::-1]

        # make tree
        nr = TreeNode()
        nr.val = array[0]
        q = deque([(nr, 0, 0)])
        
        while q:
            (node, level, idx) = q.popleft()
            if idx * 2 + 1 < n:
                node.left = TreeNode()
                node.left.val = array[idx*2+1]
                node.right = TreeNode()
                node.right.val = array[idx*2+2]

                q.append((node.left, level+1, idx*2+1))
                q.append((node.right, level+1, idx*2+2))
        return nr
