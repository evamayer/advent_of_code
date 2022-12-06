file = open("day6_input.txt")

code = list(file.readline())

result = None
i = 0
for element in code:
    four_slice = code[i:i+14]
    if len(four_slice) == len(set(four_slice)):
        break
    else:  
        i += 1   
    
result = i + 14

print(result)

file.close()