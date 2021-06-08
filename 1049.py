palavra = str(input())
palavra_2 = str(input())
palavra_3 = str(input())


if palavra == 'vertebrado':
    if palavra_2 == 'ave':
        if palavra_3 == 'carnivoro':
            print('Aguia')
        elif palavra_3 == 'onivoro':
            print('pomba')
    elif palavra_2 == 'mamifero':
        if palavra_3 == 'onivoro':
            print('homem')
        elif palavra_3 == 'herbivoro':
            print('vaca')