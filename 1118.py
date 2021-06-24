def calculate_note():
    soma = 0
    lindo = 0
    while True:
        lindo += 1
        x = float(input())
        
        if 10>=x>0:
            soma += x
        else:
            print('nova invalida')
        
        if lindo == 4:
            result = (soma/2)
            print(result)
            break

calculate_note()

def again():
    while True:
        x = int(input(''))

        if x == 1:
            calculate_note()
        elif x ==2:
            break

again()