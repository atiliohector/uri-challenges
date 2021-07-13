x = int(input())

a,b,c = 1,2,3

for i in range(x):

    print('{} {} {}'.format(a,b,c))

    a = a + 1
    b = (a**2)
    c = (a**3)