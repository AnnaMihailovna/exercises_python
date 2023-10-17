def solution(root, left=float("-inf"), right=float("+inf")):
    if not root:
        return True
    if not (left < root.value < right):
        return False
    return (solution(root.left, left=left, right=root.value)and
            solution(root.right, left=root.value, right=right))
