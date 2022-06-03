import sys
from collections import deque
input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]

blank = []
for r in range(9):
    for c in range(9):
        if sudoku[r][c] == 0:
            blank.append([r, c])
blank_pos = [[[] for _ in range(9)] for _ in range(9)]

queue = deque(blank)
while queue:
    r, c = queue.popleft()
    l = [i for i in range(1, 10)]

    for i in range(9):
        if sudoku[r][i] != 0 and sudoku[r][i] in l:
            l.remove(sudoku[r][i])
        if sudoku[i][c] != 0 and sudoku[i][c] in l:
            l.remove(sudoku[i][c])

    for i in range((r//3)*3, (r//3)*3+3):
        for j in range((c//3)*3, (c//3)*3+3):
            if sudoku[i][j] != 0 and sudoku[i][j] in l:
                l.remove(sudoku[i][j])

    if len(l) == 1:
        sudoku[r][c] = l[0]
    else:
        blank_pos[r][c].extend(l)


def func(r, c):
    if r == 9 and c == 0:
        a = True
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    a = False
        if a:
            for i in range(9):
                print(*sudoku[i])
            sys.exit()
        return
    elif r < 9:
        if sudoku[r][c] != 0:
            if c == 8:
                func(r+1, 0)
            else:
                func(r, c+1)
        else:
            for k in blank_pos[r][c]:
                p = True
                for i in range(9):
                    if sudoku[r][i] == k or sudoku[i][c] == k:
                        p = False
                for i in range((r//3)*3, (r//3)*3+3):
                    for j in range((c//3)*3, (c//3)*3+3):
                        if sudoku[i][j] == k:
                            p = False
                if p:
                    sudoku[r][c] = k
                    if c == 8:
                        func(r+1, 0)
                    else:
                        func(r, c+1)
                    sudoku[r][c] = 0


func(0, 0)
