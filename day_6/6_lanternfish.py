f = open('6_input.txt').read().split(",")

f = [int(x) for x in f]

for i in range(80):
    f = [x-1 for x in f]
    for j in range(len(f)):
        if f[j] == -1:
            f.append(8)
            f[j] = 6

answer = len(f)
print(answer)
