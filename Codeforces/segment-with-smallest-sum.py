# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
a = list(map(int, input().split()))

l = curr_s = max_len = 0

for r in range(n):
    curr_s += a[r]
    while curr_s > s:
        curr_s -= a[l]
        l += 1
    max_len = max(max_len, r-l+1)
print(max_len)


