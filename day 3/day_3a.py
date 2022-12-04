def strip(element):
    return element.strip()

def letter_to_int(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper())
    return alphabet.index(letter) + 1

file = open("day3_input.txt")
mylist = file.readlines()

stripped_list = list(map(strip, mylist))

common_letters = []
for element in stripped_list:
    firstpart, secondpart = element[:len(element)//2], element[len(element)//2:]
    test = set(firstpart).intersection(set(secondpart))
    test = list(test)
    common_letters.append(test[0])
   
common_numbers = list(map(letter_to_int, common_letters))

print(sum(common_numbers))     

file.close()

