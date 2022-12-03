file = open("day2_input.txt")
mylist = file.readlines()

stripped_list = []
right_list = []
for element in mylist:
    stripped = element.strip()
    stripped_list.append(stripped)
    split_list = stripped.split()
    right_list.append(split_list[1])
      
for i in range(len(right_list)):
    if right_list[i] == 'X':
        right_list[i] = 1
   
    if right_list[i] == 'Y':
        right_list[i] = 2

    if right_list[i] == 'Z':
        right_list[i] = 3

my_shapes = sum(right_list)

for i in range(len(stripped_list)):
    if stripped_list[i] == 'A X':
        stripped_list[i] = 3
    if stripped_list[i] == 'A Y':
        stripped_list[i] = 6
    if stripped_list[i] == 'A Z':
        stripped_list[i] = 0
    if stripped_list[i] == 'B X':
        stripped_list[i] = 0
    if stripped_list[i] == 'B Y':
        stripped_list[i] = 3
    if stripped_list[i] == 'B Z':
        stripped_list[i] = 6
    if stripped_list[i] == 'C X':
        stripped_list[i] = 6
    if stripped_list[i] == 'C Y':
        stripped_list[i] = 0
    if stripped_list[i] == 'C Z':
        stripped_list[i] = 3

my_result = sum(stripped_list)

my_total = my_shapes + my_result

print(my_total)  


file.close()

