# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
pointer = 0

for el in b:
    while pointer < n and a[pointer] < el:
        pointer += 1
    ans.append(pointer)

print(*ans)

