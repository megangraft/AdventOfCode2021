t = [int(x) for x in open('7_input.txt').read().split(",")]

sums = [0] * max(t)

for i in range(min(t), max(t)):
    sums[i] = sum([abs(x - i) for x in t])

answer = min(sums)
print(answer)