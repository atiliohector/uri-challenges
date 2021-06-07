values = [int(i) for i in input().split()]

a = values[0]
b = values[1]

if b%a==0:
    print('They are multiples')
else:
    print('They are not')