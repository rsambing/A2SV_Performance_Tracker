# https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))

l = curr_t = max_b = 0

for r in range(n):
    curr_t += a[r]

    while curr_t > t:
        curr_t -= a[l]
        l += 1
    
    max_b = max(max_b, r - l + 1)

print(max_b)
