class Node:  
    def __init__(self, left=None, right=None, value=0):  
        self.right = right
        self.left = left
        self.value = value


def insert(root, key):
    if not root:
            return Node(value=key)
    cur = root
    if key < cur.value:
        if cur.left == None:
            cur.left = Node(value=key)
            return root
        else:
            insert(cur.left, key)
    if key >= cur.value:
        if cur.right == None:
            cur.right = Node(value=key)
            return root
        else:
            insert(cur.right, key)
    return root


# def test():
#     node1 = Node(None, None, 7)
#     node2 = Node(node1, None, 8)
#     node3 = Node(None, node2, 7)
#     new_head = insert(node3, 6)
#     assert new_head is node3
#     assert new_head.left.value == 6

# if __name__ == '__main__':
#     test()