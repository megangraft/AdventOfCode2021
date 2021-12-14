import copy

f = [x.split(" -> ") for x in open('14_input.txt').read().splitlines()]

# f = {x[0] : (x[0][0]+x[1]+x[0][1]) for x in f}
f = {x[0] : x[1] for x in f}

test_start_str = 'NNCB'
start_str = 'HHKONSOSONSVOFCSCNBC'

def insertion(template, key, steps):
    for i in range(steps):
        template = list(template)
        new_template = [''] * len(template)
        for i in range(len(template) - 1):
            new_template[i] = str(template[i] + key.get(template[i]+template[i+1]))
        new_template[-1] = template[-1]
        template = ''.join(new_template)
    return ''.join(new_template)

result_str = insertion(start_str, f, 10)

most_common = max(result_str, key=result_str.count)
least_common = min(result_str, key=result_str.count)

answer = result_str.count(most_common) - result_str.count(least_common)
print(answer)