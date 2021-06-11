i = 1
j = 60

while True:
    print('i = {} j = {}'.format(i,j))
    
    j = j -5
    i = i +3
    if j == 0:
        print('over')
        break