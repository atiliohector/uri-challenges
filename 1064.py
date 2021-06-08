couting = 0
time = 0
my_little_list = []
result = 0

while True:
    
    number = float(input('Number: '))
    my_little_list.append(number)
    time += 1

    if number>0:
        couting +=1
    
    if time == 6:
        for i in my_little_list:
            if i>0:
                result = result+i
                new_result = (result/couting)
        
        print(new_result)
        print('{}'.format(couting))
        break