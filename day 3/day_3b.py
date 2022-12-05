def strip(element):
    return element.strip()

def letter_to_int(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper())
    return alphabet.index(letter) + 1

file = open("day3_input.txt")
mylist = file.readlines()

stripped_list = list(map(strip, mylist))

common_letters = []
i = 0
while i < len(stripped_list):
    test = set(stripped_list[i]) & set(stripped_list[i+1]) & set(stripped_list[i+2])
    i = i + 3
    test = list(test)
    common_letters.append(test[0])
   
common_numbers = list(map(letter_to_int, common_letters))

print(sum(common_numbers))     

file.close()