def solution(root):
    value = root.value

    def _sub(links, value):

        if links.left is not None:
            value = (links.value if value < links.value else value)
            value = _sub(links.left, value)
        if links.right is not None:
            value = (links.value if value < links.value else value)
            value = _sub(links.right, value)
        if value < links.value:
            return links.value
        else:
            return value
    value = _sub(root, value)
    return value
