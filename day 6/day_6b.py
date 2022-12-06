file = open("day6_input.txt")

code = list(file.readline())

i = 0
for element in code:
    if len(set(code[i:i+14])) == 14:
        break
    else:  
        i += 1   
    
result = i + 14

print(result)

file.close()