"""
ПРИНЦИП РАБОТЫ
    Идея удаления элемента делится на несколько случаев:
        1) у узла нет дочерних узлов;
        2) у узла есть левый дочерних узлов;
        3) у узла есть правый дочерних узлов;
        4) у узла есть оба ребёнка.

    В случае 1 просто удаляем узел, дополнительная работа не требуется.
    В случае 2 и 3 заменяем удаляемый узел на его потомка, на этом удаление заканчивается.
    В случае 4 находим в правом поддереве минимальный элемент и перемещаем его на место удаляемого узла.

    Статья - https://tproger.ru/articles/dvoichnoe-binarnoe-derevo-udalenie-jelementa-i-skorost-raboty/.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    Наихудшая временная сложность операции удаления - O(h), где h - высота дерева.
    В худшем случае нам, возможно, придется путешествовать от корня к самому глубокому узлу.
    Высота перекошенного дерева может стать n, а временная сложность операции удаления - O(n).

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Этот алгоритм использует O(h) дополнительной памяти, где h - высота дерева. 
"""


# Comment it before submitting
class Node:
    def __init__(root, left=None, right=None, value=0):
        root.right = right
        root.left = left
        root.value = value


def remove(root, key):
    if root is None:
        return root

    if root.value == key:
        if root.right and root.left:
            [psucc, succ] = _find_min(root.right, root)
            if psucc.left == succ:
                psucc.left = succ.right
            else:
                psucc.right = succ.right
            succ.left = root.left
            succ.right = root.right
            return succ
        else:
            if root.left:
                return root.left
            else:
                return root.right
    else:
        if root.value > key:
            if root.left:
                root.left = remove(root.left, key)
        else:
            if root.right:
                root.right = remove(root.right, key)
    return root


def _find_min(root, parent):
    if root.left:
        return _find_min(root.left, root)
    else:
        return [parent, root]


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8
