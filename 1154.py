add = 0
timing = 0

while True:
    x = float(input())

    if x <0:
        break

    timing +=1
    add += x

resultado = (add/timing)
print(resultado)
