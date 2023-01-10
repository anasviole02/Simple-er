
length = int(input('Length of the list :'))
my_list = []

for i in range(length):
    elements = int(input('Enter list elements :'))
    my_list.append(elements)

print(my_list)
to_find = int(input('Element to find :'))
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

