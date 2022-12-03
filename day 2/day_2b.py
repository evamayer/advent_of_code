file = open("day2_input.txt")
mylist = file.readlines()

stripped_list = []
right_list = []
for element in mylist:
    stripped = element.strip()
    stripped_list.append(stripped)
      
for i in range(len(stripped_list)):
    if stripped_list[i] == 'A X':
        stripped_list[i] = 'A C'
    if stripped_list[i] == 'A Y':
        stripped_list[i] = 'A A'
    if stripped_list[i] == 'A Z':
        stripped_list[i] = 'A B'
    if stripped_list[i] == 'B X':
        stripped_list[i] = 'B A'
    if stripped_list[i] == 'B Y':
        stripped_list[i] = 'B B'
    if stripped_list[i] == 'B Z':
        stripped_list[i] = 'B C'
    if stripped_list[i] == 'C X':
        stripped_list[i] = 'C B'
    if stripped_list[i] == 'C Y':
        stripped_list[i] = 'C C'
    if stripped_list[i] == 'C Z':
        stripped_list[i] = 'C A'

    split_list = stripped_list[i].split()
    right_list.append(split_list[1])

for i in range(len(right_list)):
    if right_list[i] == 'A':
        right_list[i] = 1
   
    if right_list[i] == 'B':
        right_list[i] = 2

    if right_list[i] == 'C':
        right_list[i] = 3

my_shapes = sum(right_list)

for i in range(len(stripped_list)):
    if stripped_list[i] == 'A C':
        stripped_list[i] = 0
    if stripped_list[i] == 'A A':
        stripped_list[i] = 3
    if stripped_list[i] == 'A B':
        stripped_list[i] = 6
    if stripped_list[i] == 'B A':
        stripped_list[i] = 0
    if stripped_list[i] == 'B B':
        stripped_list[i] = 3
    if stripped_list[i] == 'B C':
        stripped_list[i] = 6
    if stripped_list[i] == 'C B':
        stripped_list[i] = 0
    if stripped_list[i] == 'C C':
        stripped_list[i] = 3
    if stripped_list[i] == 'C A':
        stripped_list[i] = 6

my_result = sum(stripped_list)

my_total = my_shapes + my_result

print(my_total)  


file.close()