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

row_losers = [0] * int((len(rows) / 25)) # 1 index per board
column_losers = [0] * int((len(columns) / 25))
board_losers = [0] * int((len(rows) / 25))
board_start_index = 0
losing_board_index = None

loser_found = False
for num in nums:
    rows = [-1 if x == num else x for x in rows]
    columns = [-1 if x == num else x for x in columns]
    if nums.index(num) > 3: # if at least 5 numbers have been called
        for i in range(0, len(rows), 5):
            if sum(rows[i:i+5]) == -5: # if bingo found in rows
                board_start_index = int(i / 25) * 25
                row_losers[int(board_start_index / 25)] = 1
            elif sum(columns[i:i + 5]) == -5: # if bingo found in columns
                board_start_index = int(i / 25) * 25
                column_losers[int(board_start_index / 25)] = 1
            if row_losers[int(board_start_index/25)] == 1 or column_losers[int(board_start_index/25)] == 1:
                board_losers[int(board_start_index/25)] = 1
                if int(board_start_index/25) == losing_board_index:
                    board_sum = sum([x for x in rows[board_start_index:board_start_index + 25] if x != -1])
                    break
                if sum(board_losers) < len(board_losers) - 1 or loser_found == True: # continue until there's only 1 board left without a bingo
                    continue
                else:
                    loser_found = True
                    losing_board_index = board_losers.index(0)
    if loser_found == True and sum(board_losers) == len(board_losers):
        print(num * board_sum)
        break