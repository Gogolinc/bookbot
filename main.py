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

def format_report(path, number_of_words, letter_counts):
    print(f"--- Begin report of {path} ---\n")
    print(f"{number_of_words} words forund in the document \n\n")
    for lc in letter_counts:
        print(f"The '{lc}' character was found {letter_counts[lc]} times")


main()