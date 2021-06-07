values_main = [float(i) for i in input().split()]

A = values_main[0]
B = values_main[1]
C = values_main[2]

if A >= B+C:
    print('Its not a triangle')
elif (A**2) == (B**2) + (C**2):
    print('Retangulo')
elif (A**2) > (B**2) + (C**2):
    print('OBTUSANGULO')
elif (A**2) < (B**2) + (C**2):
    print('ACUTANGULO')

if A == B == C:
    print('Equilatero')
elif A==B or A==C or B==C:
    print('ISOCELES')