class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root, left=float("-inf"), right=float("+inf")):
    if not root:
        return True
    if not (left < root.value < right):
        return False
    return (solution(root.left, left=left, right=root.value)and
            solution(root.right, left=root.value, right=right))


def test():
    root1 = Node(1, None, None)
    root2 = Node(4, None, None)
    root3 = Node(3, root1, root2)
    root4 = Node(8, None, None)
    root5 = Node(5, root3, root4)

    assert solution(root5)
    root2.value = 5
    assert not solution(root5)


if __name__ == "__main__":
    test()
