def parse_input(lines):
    ranges = []
    for line in lines:
        line = line.strip()
        if "-" in line:
            a, b = map(int, line.split("-"))
            ranges.append((a, b))
    return ranges


def merge_ranges(ranges):
    ranges.sort(key=lambda r: r[0])

    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def count_ids(ranges):
    return sum((end - start + 1) for start, end in ranges)


with open('input.txt', 'r') as input:
    input_data = input.read().strip().splitlines()

ranges = parse_input(input_data)
merged = merge_ranges(ranges)
total_fresh = count_ids(merged)

print("Merged ranges:", merged)
print("Total fresh IDs:", total_fresh)
