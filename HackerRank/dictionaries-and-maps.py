# Enter your code here. Read input from STDIN. Print output to STDOUT

# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

from sys import stdin

t = int(input())
phones = {}

for _ in range(t):
    name, tel = input().split()
    phones[name] = tel

for name in stdin:
    name = name.strip()
    if name in phones:
        print(f"{name}={phones[name]}")
    else:
        print("Not found")