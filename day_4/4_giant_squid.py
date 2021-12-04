f = open('4_input.txt').read()

nums = [int(x) for x in f.splitlines()[0].split(',')]
bingo_raw = [x for x in f.splitlines()[2:] if x != '']

rows = []
for row in bingo_raw:
    row = [int(x) for x in row.split(' ') if x != '']
    for num in row:
        rows.append(num)

columns = []
high_index = 25
low_index = 0 # moves the inner loop starting range up by 1 per every 5 outer loops
for num in rows:
    for j in range(low_index, high_index, 5): # one loop for each row of 5 in this set of 25 numbers
        if j >= len(rows):
            break
        columns.append(rows[j])
    low_index += 1
    if low_index == high_index - 20: # if we've gone through all 5 sets of 5 inner loops in this set of 25 numbers
        low_index += 20
        high_index += 25

status = ''
for num in nums:
    rows = [-1 if x == num else x for x in rows]
    columns = [-1 if x == num else x for x in columns]
    if nums.index(num) > 3: # if at least 5 numbers have been called
        for i in range(0, len(rows), 5):
            if sum(rows[i:i+5]) == -5:
                status = 'bingo'
                board_start_index = int(i / 25) * 25
                board_sum = sum([x for x in rows[board_start_index:board_start_index+25] if x != -1])
                break
            elif sum(columns[i:i + 5]) == -5:
                status = 'bingo'
                board_start_index = int(i / 25) * 25
                board_sum = sum([x for x in columns[board_start_index:board_start_index + 25] if x != -1])
                break
        if status == 'bingo':
            print(num * board_sum) # answer
            break



# # original data structure I decided not to go with
# i = 0
# rows = []
# for row in bingo_raw:
#     if i == 0:
#         rows.append([])
#     row = [int(x) for x in row.split(' ') if x != '']
#     rows[-1].append(row)
#     i += 1
#     if i == 5:
#         i = 0
#
# columns = []
# for board in rows:
#     columns.append([])
#     for i in range(5):
#         columns[-1].append([])
#         for row in board:
#             columns[-1][-1].append(row[i])
