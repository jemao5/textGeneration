import numpy as np


def load_text(filepath: str):
    with open(filepath) as f:
        return f.read().lower()


def frequency_table(text: str, sample_size: int) -> dict:
    table = {}
    for i in range(0, len(text) - sample_size):
        substring = text[i:i+sample_size]
        next_char = text[i+sample_size]
        table.setdefault(substring, {})
        table[substring].setdefault(next_char, 0)
        table[substring][next_char] += 1
    return table


table = frequency_table("the them they then the then", 3)
print(table)


def calculate_probabilities(table: dict) -> None:
    for substring in table.keys():
        total = sum(table[substring].values())
        for char in table[substring].keys():
            table[substring][char] /= total


calculate_probabilities(table)
print(table)


def next_char(text: str, prob_table: dict, sample_size: int) -> str:
    substring = text[-sample_size:]
    if prob_table.get(substring) is None:
        return " "
    else:
        return np.random.choice(list(prob_table[substring].keys()), p=list(prob_table[substring].values()))


print(next_char("the", table, 3))