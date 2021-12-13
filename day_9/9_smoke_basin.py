map = open('9_input.txt').read().splitlines()

# add border numbers
for i in range(len(map)):
    map[i] = list(map[i])
    map[i].insert(0, '10')
    map[i].append('10')
map.insert(0, ['10']*len(map[0]))
map.append(['10']*len(map[0]))

i = 1
risk = 0

for line in map[1:-1]:
    for k, v in enumerate(line[1:-1]):
        v = int(v)
        # if the number is less than the numbers above, below, to the right, and left of it:
        if v < int(map[i-1][k+1]) and v < int(map[i+1][k+1]) and v < int(line[k+2]) and v < int(line[k]):
            risk += v
            risk += 1
    i += 1

answer = risk
print(answer)
