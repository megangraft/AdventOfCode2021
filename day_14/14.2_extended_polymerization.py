import collections
import itertools

f = [x.split(" -> ") for x in open('14_input.txt').read().splitlines()]

# f = {x[0] : (x[0][0]+x[1]+x[0][1]) for x in f}
f = {x[0] : x[1] for x in f}

# start_str = 'NNCB'
start_str = 'HHKONSOSONSVOFCSCNBC'
steps = 40

counts = collections.Counter()

for pair in itertools.pairwise(start_str):
    counts[pair[0]+pair[1]] += 1

for i in range(steps-1):
    new_counts = collections.Counter()
    for k, v in counts.items():
        new_counts[k[0]+f.get(k)] += v
        new_counts[f.get(k)+k[1]] += v
    counts = new_counts

alphabet = [0] * 26

for k, v in counts.items():
    alphabet[ord(k[0])-65] += v
    alphabet[ord(f.get(k))-65] += v

alphabet[ord(start_str[-1])-65] += 1

answer = max([x for x in alphabet if x != 0]) - min([x for x in alphabet if x != 0])
print(answer)

# big thank you to anthonywritescode on YouTube for his helpful breakdown of Part II
# New learnings: collections library, pairwise, Counter, long string algorithms
