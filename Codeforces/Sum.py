# https://codeforces.com/problemset/problem/1742/A

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    if c == a + b or b == a + c or a == b + c:
        print("YES")
    else:
        print("NO")
