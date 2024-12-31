def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words_in_book(text)
    letter_counts = count_letters(text)
    print(f"\nLetter counts:   {letter_counts}")

def get_book_text(path):
    with open(path) as f:
       return f.read()

def count_words_in_book(t):
    words = t.split()
    return len(words)

def count_letters(text):
    lowered_string = text.lower()
    letter_counts = {}
    for char in lowered_string:
        letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts


main()