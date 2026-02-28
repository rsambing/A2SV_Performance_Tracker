t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    if any(abs(a[i+1] - a[i]) > 1 for i in range(n-1)):
        print("NO")
    else:
        print("YES")
