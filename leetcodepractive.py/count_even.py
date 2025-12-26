lista = list(map(int, input().strip("[]").split(",")))
n = len(lista)
count = 0
for i in range (0, n):
    if lista[i] % 2 == 0:
        count += 1
print(count)
    