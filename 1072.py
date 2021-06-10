n = int(input())

in_total = 0
out_total = 0

for i in range(n):
    x = int(input())

    if x<=10<=20:
        in_total += 1
    else:
        out_total +=1

print('{} in'.format(in_total))
print('{} out '.format(out_total))