soma = 0
lindo = 0

while True:
    a = float(input())

    if a<0 or a >10:
        print('nota invalida')
    elif 10>=a>0:
        soma+=a
        lindo +=1
        if lindo == 2:
            result = (soma/2)
            print(result)
            break
    
