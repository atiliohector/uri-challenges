values = [float(i) for i in input().split()]

a = values[0]
b = values[1]
c = values[2]

soma_1 = (a+b)
soma_2 = int(a-b)

if c<soma_1 and c>soma_2:
    perimeter = (a+b+c)
    print('Perimeter = {}'.format(perimeter))
else:
    area = (((a+b)*c)/2)
    print('Area = {}'.format(area))
