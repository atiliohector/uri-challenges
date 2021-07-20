N = int(input())

listinha = []
soma = 0

x = int(input())
y = int(input())

if x %2 !=0:
    soma += x

for m in range(N):
    
    add = 0
    
    while True:
        x += 1
        add += 1
        listinha.append(x)
        if add == y:
            break

for d in listinha:
    if d%2!=0:
        soma += d

print(soma)
    