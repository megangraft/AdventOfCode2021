import itertools

t = [int(x) for x in open('7_input.txt').read().split(",")]

sums = [0] * max(t)
fuel = []
agg_fuel = [0]

for i in range(max(t)):
    fuel.append(i+1)

for i in itertools.accumulate(fuel):
    agg_fuel.append(i)

for i in range(min(t), max(t)):
    sums[i] = sum([agg_fuel[abs(x - i)] for x in t])

answer = min(sums)
print(answer)