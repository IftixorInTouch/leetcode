with open("input.txt") as input_file:
    data = input_file.read().splitlines()

position = 50
number_of_zeros = 0

for move in data:
    direction = move[0]
    step = int(move[1:])
    if direction == 'L':
        position = (position - step) % 100
    elif direction == 'R':
        position = (position + step) % 100
    else:
        print('Invalid move')
        exit(1)

    if position == 0:
        number_of_zeros += 1
print(number_of_zeros)
