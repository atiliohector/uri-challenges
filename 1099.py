x = int(input())

for i in range(x):
    c = [int(i) for i in input().split()]
    
    a = c[0]
    b = c[1] 

    if a>b:
        for f in range(a+1,b):
            if f%2 != 0:
                f += f
                print(f)
    elif b>a:
        for l in range(b+1,a):
            if l%2 !=0:
                print(l)
    elif a == b:
        print(0)