# https://codeforces.com/problemset/problem/263/A

matrix = [list(map(int, input().split())) for _ in range(5)]

pos = None

for i, line in enumerate(matrix):
    for j, value in enumerate(line):
        if value == 1:
            pos = (i, j)
            break
    if pos:
        break

print(f"{abs(i - 2) + abs(j - 2)}")
