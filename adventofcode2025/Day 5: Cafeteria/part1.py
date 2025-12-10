def get_fresh_ingredients():
    ingredients_id_range = []
    result = 0
    with open('input.txt', 'r') as input:
        for line in input:
            if "-" in line:
                ingredients_id_range.append(list(map(int, line.split("-"))))
            elif line not in ['\n', '\r', '\r\n']:
                for ingredient in ingredients_id_range:
                    if int(line) in range(ingredient[0], ingredient[1] + 1):
                        result += 1
                        break

    return result


if __name__ == "__main__":
    print(get_fresh_ingredients())
