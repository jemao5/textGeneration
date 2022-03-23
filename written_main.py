def frequency_table(text: str, sample_size: int):
    table = {}
    for i in range(0, len(text) - sample_size):
        substring = text[i:i+sample_size]
        next_char = text[i+sample_size]
        table.setdefault(substring, {})
        table[substring].setdefault(next_char, 0)
        table[substring][next_char] += 1
    return table


print(frequency_table("the them they then the then", 3))

