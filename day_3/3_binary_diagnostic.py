f = open('3_input.txt').read().splitlines()

gamma = [0] * 12
epsilon = [0] * 12

for line in f:
    i = 0
    for char in line:
        gamma[i] += int(char)
        i += 1

for i in range(len(gamma)):
    if gamma[i] < len(f) / 2:
        gamma[i], epsilon[i] = '0', '1'
    else:
        gamma[i], epsilon[i] = '1', '0'

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

answer = gamma * epsilon