x = int(input())

a,b,c=1,2,3

for i in range(x):

    print('{} {} {} PUM'.format(a,b,c))

    a = c + 2
    b = a + 1
    c = b + 1