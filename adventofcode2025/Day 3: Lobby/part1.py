def largest_possible_joltage():
    with open("input.txt") as input_file:
        banks = map(str, input_file.read().splitlines())

    result = 0
    for bank in banks:
        left_max = int(bank[0])
        best = -1
        for digit in map(int, bank[1:]):
            current = 10 * left_max + digit
            if current > best:
                best = current
            if digit > left_max:
                left_max = digit
        result += best
    return result


if __name__ == "__main__":
    print(largest_possible_joltage())
