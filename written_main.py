import numpy as np


def load_text(filepath: str, filetype: str = "txt"):
    if filetype == "txt":
        with open(filepath, encoding='utf8') as f:
            return f.read().lower()
    # elif filetype is "pdf":
    #     with open(filepath) as f:


def frequency_table(text: str, sample_size: int) -> dict:
    table = {}
    for i in range(0, len(text) - sample_size):
        substring = text[i:i+sample_size]
        next_char = text[i+sample_size]
        table.setdefault(substring, {})
        table[substring].setdefault(next_char, 0)
        table[substring][next_char] += 1
    return table



def calculate_probabilities(table: dict) -> None:
    for substring in table.keys():
        total = sum(table[substring].values())
        for char in table[substring].keys():
            table[substring][char] /= total


def next_char(text: str, prob_table: dict, sample_size: int) -> str:
    substring = text[-sample_size:]
    if prob_table.get(substring) is None:
        return " "
    else:
        # return np.random.choice(list(prob_table[substring].keys()), p=list(prob_table[substring].values()))
        return list(prob_table[substring].keys())[np.argmax(prob_table[substring].keys())]


def all_together(text_size: int):
    sampletext = load_text("stateoftheunion.txt")
    markov_table = frequency_table(sampletext, 5)
    calculate_probabilities(markov_table)

    final_output = "the u"

    for i in range(0, text_size):
        final_output += next_char(final_output.lower(), markov_table, 5)

    file = open("./output.txt", 'w')
    file.write(final_output)


all_together(1000)
