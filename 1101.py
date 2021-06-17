m,n = [int(i) for i in input().split()]

while True:
    if m == 0 or n == 0:
        break
    
    if m>n:
        sum = 0
        listinha_1 = []
        for i in range(n,m+1):
            sum += i
            listinha_1.append(i)
        print(*listinha_1, sep=' ')
        print(sum)
        break
    elif n>m:
        sum = 0
        listinha_2 = []
        for i in range(m,n+1):
            listinha_2.append(i)
            sum += i
        print(*listinha_2)
        print(sum)
        break