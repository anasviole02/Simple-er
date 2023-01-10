list = [50, 12, 13, 25, 22]
print('Unsorted list :', list)
print('Sorting :')
for i in range(len(list)):
    low = i
    for j in range(i + 1, len(list)):
        if list[low] > list[j]:
            low = j

    list[i], list[low] = list[low], list[i]

    print(list)

print('Sorted list :', list)
