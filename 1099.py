x = int(input())

for i in range(x):
    c = [int(i) for i in input().split()]
    
    a = c[0]
    b = c[1] 

    if a>b:
        soma = 0
        for f in range(b+1,a):
            if f%2 != 0:
                soma += f
        print(soma)
    elif b>a:
        soma = 0
        for l in range(a+1,b):
            if l%2 !=0:
                soma+=l
        print(soma)
    elif a == b:
        print(0)