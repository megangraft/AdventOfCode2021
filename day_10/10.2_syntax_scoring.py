f = open('10_input.txt').read().splitlines()

for i in range(len(f)):
    f[i] = list(f[i])

valid_pairs = {']':'[', '}':'{', ')':'(', '>':'<'}
point_values = {'[':2, '{':3, '(':1, '<':4}

error_queue = []
score = 0
scores = []

for line in f:
    for char in line:
        if char in valid_pairs.keys():
            if error_queue[-1] == valid_pairs.get(char): # if corrupt, move on to next line
                error_queue.pop(-1)
            else:
                stop_loop = True
                break
        else:
            error_queue.append(char)
    if stop_loop == True:
        stop_loop = False
        score = 0
        error_queue = []
        continue
    error_queue.reverse()
    for char in error_queue:
        score *= 5
        score += point_values.get(char)
    scores.append(score)
    score = 0
    error_queue = []

scores.sort()
answer = scores[int(len(scores)/2)]
print(answer)
