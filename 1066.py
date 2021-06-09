odd = 0
positive = 0
negative = 0
pair = 0

quantity = 0

while True:
    
    number = int(input())

    if number%2==0:
        if number <0:
            negative +=1
        pair +=1
    elif number%2 != 0:
        if number <0:
            negative +=1
        odd +=1
    elif number %2 ==0:
        if number >0:
            positive +=1
        pair +=1
    elif number %2 !=0:
        if number >0:
            positive +=1
        pair +=1

    quantity +=1 

    if quantity == 5:
        print('Over')
        print(pair)
        print(odd)
        print(positive)
        print(negative)
        break