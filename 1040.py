numbers = [float(i) for i in input().split()]

A = numbers[0]
B = numbers[1]
C = numbers[2]
D = numbers[3]

# 2 3 4 1
media = ((A*2)+(B*3)+(C*4)+(D*1))/10

if media>= 7.0:
    print('Media: {:.1f}'.format(media))
    print('Approved student')
elif media <= 6.9 and media >=5.0:
    print('Media: {:.1f}'.format(media))
    print('Student in exam')
    new_note = float(input())
    print('Exame note: {:.1f}'.format(new_note))
    new_media = (new_note+media)/2
    if new_media >5.0:
        print('Approved student')
    elif new_media<4.9:
        print('Disapproved student')
elif media < 5.0:
    print('Media: {:.1f}'.format(media))
    print('Disapproved student')
