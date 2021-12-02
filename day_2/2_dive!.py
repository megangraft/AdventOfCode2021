f = open('2_input.txt').read().splitlines()

down = sum([int(x[-1]) for x in f if 'down' in x])
forward = sum([int(x[-1]) for x in f if 'forward' in x])
up = sum([int(x[-1]) for x in f if 'up' in x]) * -1

answer = (down + up) * forward