def add_invalid_ids(filename: str) -> int:
    with open(filename) as f:
        ranges = f.read().split(",")
    invalid_ids_sum = 0
    for data in ranges:
        first_id, second_id = map(int, data.split("-"))
        for i in range(first_id, second_id + 1):
            str_id = str(i)
            if str_id[:len(str_id) // 2] == str_id[len(str_id) // 2:]:
                invalid_ids_sum += i
    return invalid_ids_sum


if __name__ == "__main__":
    answer = add_invalid_ids("input.txt")
    print(answer)
