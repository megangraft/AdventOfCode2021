f = open('10_input.txt').read().splitlines()

for i in range(len(f)):
    f[i] = list(f[i])

valid_pairs = {']':'[', '}':'{', ')':'(', '>':'<'}
score_values = {']':57, '}':1197, ')':3, '>':25137}

error_queue = []
errors = []
score = 0

for line in f:
    for char in line:
        if char in valid_pairs.keys():
            if error_queue[-1] == valid_pairs.get(char):
                error_queue.pop(-1)
            else:
                errors.append(char)
                score += score_values.get(char)
                error_queue.pop(-1)
        else:
            error_queue.append(char)

answer = score
print(answer)
