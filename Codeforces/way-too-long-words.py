n = int(input())
for _ in range(n):
    s = input()
    count = len(s)
    if (count > 10):
        print(f"{s[0]}{count - 2}{s[-1]}")
    else:
        print(s)