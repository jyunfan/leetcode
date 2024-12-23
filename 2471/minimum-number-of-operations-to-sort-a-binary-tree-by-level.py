from collections import defaultdict

def count_swap_need(A):
    visited = set()
    dest = {}
    S = sorted(A)

    # Find the expected location of number S_i
    for i in range(len(S)):
        dest[S[i]] = i

    # for example
    # 5 2 6 1 4
    # in order:
    # 1 2 4 5 6
    # so number 5 should be at location 3
    counter = 0
    for i in range(len(A)):
        if A[i] in visited:
            continue

        x = A[i]
        while True:
            visited.add(x)
            n_idx = dest[x]
            x = A[n_idx]
            if x in visited:
                break
            counter += 1
    return counter
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, level):
        self.L[level].append(node.val)

        if node.left:
            self.dfs(node.left, level+1)

        if node.right:
            self.dfs(node.right, level+1)

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # convert the tree to an array
        self.L = defaultdict(list)
        self.dfs(root, 0)

        # sort each level
        counter = 0
        for key in self.L.keys():
            data = self.L[key]
            if len(data) <= 1:
                continue
            counter += count_swap_need(data)
        return counter

