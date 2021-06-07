values_main = [int(i) for i in input().split()]

A = values_main[0]
B = values_main[1]

if B>A:
    resultado = B-A
    print('{} horas'.format(resultado))
elif A>B:
    resultado = (24-A)+B
    print('{} horas'.format(resultado))
elif A==B:
    print('24 horas')