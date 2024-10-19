"""
BFS: TC O(n) and SC: O(n/2) max nodes at last level. For the pop from deque syntax is: popleft().
DFS:
why the level parameter is local?
Assuming it is global, when the recursion returns from left child (at level 3) to parent (at level 2) and goes to right
child, its level would be 4.
how to store each level node?
Use hmap with keys as level and values as the list. How to return, while maintaining the order?
To return in the same order, use min and max and iterate through the hmap this is called BUCKET SORT. why? because
under the hood, hmap stores items in bucket.
 If not using the hmap to maintain the order, use the Tree map then TC would be logarithm and if linked hmap
 are used, then under the hood they use queue, thus going for extra space.
 TC: O(n) tree traversal + O(n) for traversing the hmap
 SC: O(h) for traversal + O(n) for hmap

Alternate to hmap:
use the array. The index could be the level.
# DFS: TC: O(n) and SC: O(h)
When list initialization and appending to list are done in in-order way, there will be error because the level is
increased but the list is not initialized, will give out of bound error. To make it work, when the leaf node is
 reached, initilize the list with a legth of existing legth of list -  level.
"""
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution_bfs:
    def bfs(self, root, ans):
        # define a queue
        q = deque()
        # add the root to the deque
        q.append(root)

        # traverse the queue until empty
        while q:
            # define a size variable to keep track of level
            size = len(q)
            # to add node at each level
            temp = []
            # traverse the level
            for _ in range(size):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            ans.append(temp)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if not root:
            return ans

        self.bfs(root, ans)
        return ans

class Solution_dfs:
    def dfs_2(self, node, level, ans):
        # base case
        if not node:
            return

        self.dfs(node.left, level + 1, ans)

        if len(ans) <= level:
            for _ in range(len(ans), level + 1):
                ans.append([])

        ans[level].append(node.val)
        self.dfs(node.right, level + 1, ans)
        
    def dfs(self, node, level, ans):

        # base case
        if not node:
            return

        # if level number is equal to size of and list it means the level is reached the first time
        # initilize the list
        if level == len(ans):
            ans.append([])
        ans[level].append(node.val)

        self.dfs(node.left, level + 1, ans)
        self.dfs(node.right, level + 1, ans)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.dfs(root, 0, ans)
        return ans

