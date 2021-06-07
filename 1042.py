values = [int(i) for i in input().split()]

a = values[0]
b = values[1]
c = values[2]

my_list = []
my_list.append(a)
my_list.append(b)
my_list.append(c)

regular_list = sorted(my_list)

new_a = regular_list[0]
new_b = regular_list[1]
new_c = regular_list[2]

print(new_a)
print(new_b)
print(new_c)

print('')

print(a)
print(b)
print(c)