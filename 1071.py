x = int(input())
y = int(input())

quantify = 0

if x>y:
    for i in range(y,x):
        if i%2 !=0 and i >0:
            quantify += i
            print(quantify)
elif y>x:
    for i in range(x,y):
        if i%2 !=0:
            quantify+=1
            print(quantify)
elif x==y:
    print(0)