f = open('2_input.txt').read().splitlines()

aim = 0
horiz = 0
depth = 0

for x in f:
    if x[:-2] == 'down':
        aim += int(x[-1])
    elif x[:-2] == 'up':
        aim += int(x[-1]) * -1
    else:
        horiz += int(x[-1])
        depth += aim * int(x[-1])

answer = horiz * depth

print(answer)