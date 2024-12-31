import re
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words_in_book(text)
    letter_counts = count_letters(text)
    format_report(book_path, number_of_words, letter_counts)

def get_book_text(path):
    with open(path) as f:
       return f.read()

def count_words_in_book(t):
    words = t.split()
    return len(words)

def count_letters(text):
    lowered_string = text.lower()
    lowered_string = re.sub(r'[^A-Za-z\\s]', '', lowered_string)
    letter_counts = {}
    for char in lowered_string:
        letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

#indicates what a list should use as a comparator value
def sort_on(d):
    return d["num"]

def convert_char_dict_to_sorted_list(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def format_report(path, number_of_words, letter_counts):
    sorted_letter_counts = convert_char_dict_to_sorted_list(letter_counts)
    print(f"--- Begin report of {path} ---\n")
    print(f"{number_of_words} words found in the document \n\n")
    for lc in sorted_letter_counts:
        print(f"The '{lc['char']}' character was found {lc['num']} times")


main()