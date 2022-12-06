file = open("day6_input.txt")

code = list(file.readline())

i = 0
for element in code:
    if len(set(code[i:i+4])) == 4:
        break
    else:  
        i += 1   
    
result = i + 4

print(result)

file.close()