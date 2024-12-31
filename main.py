def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words_in_book(text)
    print(f"\nNumber of words:   {number_of_words}")

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        print(f.read())

def count_words_in_book(text):
    words = text.split()
    return len(words)

main()