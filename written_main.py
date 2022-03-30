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


def next_word(text: str, index: int):
    i = 1
    while index+i < len(text) and (text[index+i] != " " and text[i] != "\n"):
        i += 1
    return text[index+1:index+i].replace(".", "")


def previous_word(text: str):
    i = len(text) - 1
    while i >= 0 and (text[i] != " " and text[i] != "\n"):
        i -= 1
    return text[i+1:].replace(".", "")


def frequency_table(text: str, sample_size: int) -> dict:
    table = {}
    for i in range(0, len(text) - sample_size):
        substring = text[i:i+sample_size]
        next_char = text[i+sample_size]
        table.setdefault(substring, {})
        table[substring].setdefault(next_char, 0)
        table[substring][next_char] += 1
    # count = len(text)
    # word_length = 0
    # for i in range(0, len(text)):
    #     if count > 0:
    #         if text[i] != " " and text[i] != "\n":
    #             word_length += 1
    #         else:
    #             substring = text[i-word_length:i].replace(".", "")
    #             next_char = next_word(text, i)
    #             # print(next_char)
    #             table.setdefault(substring, {})
    #             table[substring].setdefault(next_char, 0)
    #             table[substring][next_char] += 1
    #             count -= (word_length+1)
    #             word_length = 0
    #             i+=1
    return table


table = frequency_table("the them they then the then", 3)
print(table)


def calculate_probabilities(table: dict) -> None:
    for substring in table.keys():
        total = sum(table[substring].values())
        for char in table[substring].keys():
            table[substring][char] /= total


# calculate_probabilities(table)
# print(table)


def next_char(text: str, prob_table: dict, sample_size: int) -> str:
    substring = text[-sample_size:]
    # substring = previous_word(text)
    # print(substring)
    if prob_table.get(substring) is None:
        return " "
    else:
        return np.random.choice(list(prob_table[substring].keys()), p=list(prob_table[substring].values()))
        # return list(prob_table[substring].keys())[np.argmax(prob_table[substring].keys())]


def all_together(filename: str, text_size: int, starter_word: str = "Them a", sample_size: int = 3) -> None:
    sample_text = load_text(filename)
    sample_text = " ".join(sample_text.split())
    markov_table = frequency_table(sample_text, sample_size)
    print(markov_table)
    calculate_probabilities(markov_table)
    # print(markov_table)
    final_output = starter_word

    for i in range(0, text_size):
        word = next_char(final_output.lower(), markov_table, sample_size)
        # if (i+1) % 50 == 0:
        #     final_output += "\n" + word
        # else:
        #     final_output += " " + word
        final_output += " " + word

    final_output += "."
    file = open("./output.txt", 'w')
    file.write(final_output)


all_together("stateoftheunion.txt", 1000, "Them a", 6)
