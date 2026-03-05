# https://codeforces.com/problemset/problem/1174/B

n = int(input())
a = list(map(int, input().split()))

if all(x % 2 == 0 for x in a) or all(x % 2 != 0 for x in a):
    print(*a)
else:
    print(*sorted(a))

