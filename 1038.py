values = [int(i) for i in input().split()]

code = values[0]
quantity = values[1]

price = 0

if code == 1:
    price = 4.0
    value = (price*quantity)
    print('Total: R$ {:.2f}'.format(value))
elif code ==2:
    price = 4.5
    value = (price*quantity)
    print('Total: R$ {:.2f}'.format(value))
elif code ==3:
    price = 5.0
    value = (price*quantity)
    print('Total: R$ {:.2f}'.format(value))
elif code ==4:
    price = 2.0
    value = (price*quantity)
    print('Total: R$ {:.2f}'.format(value))
elif code ==5:
    price = 1.5
    value = (price*quantity)
    print('Total: R$ {:.2f}'.format(value))
