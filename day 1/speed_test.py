import time

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

# get the start time
st = time.time()

# totals_list.sort(reverse=True)

for i in range(10000000):
    # sum_three = totals_list[0] + totals_list[1] + totals_list[2]
    sum_three = sum(totals_list[-3:])

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')