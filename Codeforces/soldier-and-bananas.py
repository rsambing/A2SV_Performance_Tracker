k, n, w = list(map(int, input().split()))
 
soma = 0
for i in range(1, w+1):
    soma += i * k
print(max(0, soma - n))
