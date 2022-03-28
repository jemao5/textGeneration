import numpy as np
import PyPDF2 as pr


def load_text(filepath: str, filetype: str = "txt") -> str:
    if filetype == "txt":
        with open(filepath, encoding='utf8') as f:
            return f.read().lower()
    elif filetype == "pdf":
        with open(filepath, "rb") as f:
            pdf_reader = pr.PdfFileReader(f)
            return pdf_reader.getPage(0).extractText()


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
        return np.random.choice(list(prob_table[substring].keys()), p=list(prob_table[substring].values()))
        # return list(prob_table[substring].keys())[np.argmax(prob_table[substring].keys())]


def all_together(starter_word: str, filename: str, text_size: int, sample_size: int = 3) -> None:
    sample_text = load_text(filename)
    markov_table = frequency_table(sample_text, sample_size)
    print(markov_table)
    calculate_probabilities(markov_table)
    print(markov_table)
    final_output = starter_word

    for i in range(0, text_size):
        final_output += next_char(final_output.lower(), markov_table, sample_size)

    file = open("./output.txt", 'w')
    file.write(final_output)


all_together("Them ", "stateoftheunion.txt", 1000, 3)
