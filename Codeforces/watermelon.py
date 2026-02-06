# https://codeforces.com/problemset/problem/4/A

n = int(input())

n -= 2
if (n <= 0 or n % 2 != 0):
    print("NO")
else:
    print("YES")
