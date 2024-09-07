def solveNQueens(n) -> List:
    cols = set()
    posDia = set() # (r - c)
    negDia = set() # (r + c)

    board = [['.'] * n for r in range(n)]
    res = []

    def backtrack(r):
        if r == n:
            copy = ["".join(row)  for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in board or (c+r) in negDia or (r-c) in posDia:
