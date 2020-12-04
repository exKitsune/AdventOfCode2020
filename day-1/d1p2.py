with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

#2020 - x where x = y + z
list_2 = []
for i in input_file:
    list_2.append(2020 - int(i))

#calculating all values of y + z
list_3 = []
i = 0
while i < len(input_file) - 1:
    for j in input_file[i+1:]:
        list_3.append(int(input_file[i]) + int(j))
    i += 1

#finding all occurences of (y+z) in list_2
dupe_numbers = []
for i in list_2:
    if i in list_3:
        dupe_numbers.append(i)

#413, 1824, 1803, 3 numbers, 3 sums
#choose 1 sum
#413 - x where x = y + z, we want to find the y and z
list_4 = []
for i in input_file:
    list_4.append(dupe_numbers[0] - int(i)) 

dupe_numbers_2 = []
for i in list_4:
    if str(i) in input_file:
        dupe_numbers_2.append(i)

third_number = 0
for i in input_file:
    if (2020 - int(i)) == dupe_numbers_2[0] + dupe_numbers_2[1]:
        third_number = int(i)

print(dupe_numbers_2[0] * dupe_numbers_2[1] * third_number)