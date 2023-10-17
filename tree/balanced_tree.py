# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left

def dfs(root):
    if root is None:
        return 0
    return max(dfs(root.left), dfs(root.right)) + 1


def solution(root):
    if root is None:
        return True
    l_depth = dfs(root.left)
    r_depth = dfs(root.right)
    if (solution(root.left) and solution(root.right) and
        abs(l_depth-r_depth) <= 1):
        return True
    return False


# def test():
#     node1 = Node(1)
#     node2 = Node(-5)
#     node3 = Node(3, node1, node2)
#     node4 = Node(10)
#     node5 = Node(2, node3, node4)
#     assert solution(node5)


# if __name__ == "__main__":
#     test()