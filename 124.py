"""
124. 二叉树中的最大路径和
https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(arr: list[Optional[int]]) -> Optional[TreeNode]:
    l = len(arr)

    if len(arr) == 0 or arr[0] is None:
        return None

    root = TreeNode(arr[0], None, None)
    queue: list[Optional[TreeNode]] = [root]

    i = 1
    while len(queue) > 0:
        next_queue: list[Optional[TreeNode]] = []
        for n in queue:
            if i >= l:
                break
            left = None if arr[i] is None else TreeNode(arr[i], None, None)
            n.left = left
            if left:
                next_queue.append(left)
            i = i + 1

            if i >= l:
                break
            right = None if arr[i] is None else TreeNode(arr[i], None, None)
            n.right = right
            if right:
                next_queue.append(right)
            i = i + 1

        queue = next_queue

    return root


def print_binary_tree(root: Optional[TreeNode]):
    if root is None:
        return

    queue = [root]

    while len(queue) > 0:
        next_queue = []
        is_empty = True

        for n in queue:
            if n is None:
                print("null")
                continue

            print(n.val)

            next_queue.append(n.left)
            next_queue.append(n.right)

            is_empty = is_empty and (n.left is None) and (n.right is None)

        if is_empty:
            queue = []
        else:
            queue = next_queue


class Solution:
    def __init__(self) -> None:
        self.result = -1000 * 3 * (10**4)

    def max_gain(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        """ 
        If the max gain is less than 0, set it to 0.
        This means that the end of the path does not have to be the leaf node.
        """
        left_max_gain = max(self.max_gain(node.left), 0)
        right_max_gain = max(self.max_gain(node.right), 0)

        sum = node.val + left_max_gain + right_max_gain
        if sum > self.result:
            self.result = sum

        return node.val + max(left_max_gain, right_max_gain)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_gain(root)
        return self.result


if __name__ == "__main__":
    s = Solution()

    root = create_binary_tree(
        [9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6]
    )

    print(s.maxPathSum(root))
