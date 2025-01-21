def generate_case_variations(s):
    if not s:  # Base case: if the string is empty, return an empty string
        return [""]

    # Get the first character and the rest of the string
    first_char = s[0]
    rest = s[1:]

    # Recursively get case variations for the rest of the string
    rest_variations = generate_case_variations(rest)

    # Generate variations for the first character (case-sensitive if it's a letter)
    if first_char.isalpha():
        first_variations = [first_char.lower(), first_char.upper()]
    else:
        first_variations = [first_char]

    # Combine the first character variations with the rest of the string variations
    result = []
    for variant in first_variations:
        for rest_variant in rest_variations:
            result.append(variant + rest_variant)

    return result

# Example usage
# input_string = "a1b2"
# variations = generate_case_variations(input_string)
# print(variations)
s = "1helo"
a = "a"
print(isinstance(a, str))