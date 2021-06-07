values = [float(i) for i in input().split()]

x = values[0]
y = values[1]

if x==y==0:
    print('Origin')
elif x>0 and y>0:
    print('Q1')
elif x<0 and y>0:
    print('Q2')
elif x<0 and y<0:
    print('Q3')
elif x>0 and y<0:
    print('Q4')