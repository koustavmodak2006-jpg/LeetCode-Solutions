class Node:
    def __init__(self):
        self.left_char = ''
        self.right_char = ''
        self.left_len = 0
        self.right_len = 0
        self.best = 0
        self.length = 0


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:

        n = len(s)
        tree = [Node() for _ in range(4 * n)]

        def merge(a, b):
            if a.length == 0:
                return b
            if b.length == 0:
                return a

            res = Node()
            res.length = a.length + b.length

            res.left_char = a.left_char
            res.right_char = b.right_char

            res.left_len = a.left_len
            res.right_len = b.right_len

            if a.left_len == a.length and a.right_char == b.left_char:
                res.left_len += b.left_len

            if b.right_len == b.length and a.right_char == b.left_char:
                res.right_len += a.right_len

            res.best = max(a.best, b.best)

            if a.right_char == b.left_char:
                res.best = max(res.best, a.right_len + b.left_len)

            return res

        def build(node, l, r):
            if l == r:
                tree[node].left_char = s[l]
                tree[node].right_char = s[l]
                tree[node].left_len = 1
                tree[node].right_len = 1
                tree[node].best = 1
                tree[node].length = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node].left_char = ch
                tree[node].right_char = ch
                tree[node].left_len = 1
                tree[node].right_len = 1
                tree[node].best = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1].best)

        return ans