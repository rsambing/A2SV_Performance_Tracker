n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
l = r = 0

while l < n and r < m:
    if a[l] <= b[r]:
        ans.append(a[l])
        l += 1
    else:
        ans.append(b[r])
        r += 1

ans += a[l:]
ans += b[r:]

print(*ans)
