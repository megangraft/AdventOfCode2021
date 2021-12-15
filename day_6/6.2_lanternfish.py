import collections

f = open('6_input.txt').read().split(",")

f = collections.Counter([int(x) for x in f])

for i in range(256):
    fish_count = collections.Counter()
    for k, v in f.items():
        fish_count[k-1] += v
        if -1 in fish_count.keys():
            fish_count[8] += v
            fish_count[6] += v
            del fish_count[-1]
    f = fish_count

answer = f.total()
print(answer)
