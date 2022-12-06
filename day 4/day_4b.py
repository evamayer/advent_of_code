def strip(element):
    return element.strip()

file = open("day4_input.txt")

stripped_list = list(map(strip, file.readlines()))

counts = 0
for element in stripped_list:
    a, b = element.split(',')
    c, d = a.split('-'), b.split('-')
    c = list(map(int, c))
    d = list(map(int, d))
    rng1 = set(range(c[0], c[1] + 1))
    rng2 = set(range(d[0], d[1] + 1))
    if rng1.isdisjoint(rng2) is False:
        counts += 1

print(counts)

file.close()
