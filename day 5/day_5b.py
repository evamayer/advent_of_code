file = open("day5_input.txt")

moves = file.readlines()

instructions = []
for element in moves:
    split_list = element.split(' ')
    number_list = split_list[1::2]
    number_list = list(map(int, number_list))
    instructions.append(number_list)

stack1 = ['M', 'J', 'C', 'B', 'F', 'R', 'L', 'H']
stack2 = ['Z', 'C', 'D']
stack3 = ['H', 'J', 'F', 'C', 'N', 'G', 'W']
stack4 = ['P', 'J', 'D', 'M', 'T', 'S', 'B']
stack5 = ['N', 'C', 'D', 'R', 'J']
stack6 = ['W', 'L', 'D', 'Q', 'P', 'J', 'G', 'Z']
stack7 = ['P', 'Z', 'T', 'F', 'R', 'H']
stack8 = ['L', 'V', 'M', 'G']
stack9 = ['C', 'B', 'G', 'P', 'F', 'Q', 'R', 'J']

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

for el in instructions:
    a = el[0]   
    b = el[1]   
    c = el[2] 
    
    for p in reversed(range(1, a+1)):
        x = stacks[b-1].pop(-p)
        stacks[c-1].append(x)

result = []

for piles in stacks:
    top_crate = piles.pop(-1)
    result.append(top_crate)

print("".join(result))

file.close()