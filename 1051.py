number_imaginary = float(input())


if 0<number_imaginary<=2000:
    print('no tax')
elif 2000.01<number_imaginary<=3000:
    tax = 0.08
    result = (number_imaginary*tax)
    print('tax = {}'.format(result))
elif 3000.01<number_imaginary<=4500:
    tax = 0.18
    result = (number_imaginary*tax)
    print('tax = {}'.format(result))
elif number_imaginary>4500:
    tax = 0.28
    result = (number_imaginary*tax)
    print('tax = {}'.format(result))
