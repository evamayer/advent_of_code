file = open("day1_input.txt")
mylist = file.readlines()

mylist.append("")
addition = 0
totals_list = []

for element in mylist:
    stripped = element.strip()
    if stripped != "":
        addition = addition + int(stripped)
    else:
        section_total = addition
        totals_list.append(section_total)
        addition = 0

print(max(totals_list))     

file.close()
