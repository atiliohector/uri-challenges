N = int(input())

listinha = []
prod = 1

for i in range(1,N+1):
    listinha.append(i)

for j in listinha:
    prod *= j

print(prod)