from stats import get_num_words, get_num_chars


def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()


def main():
    text = get_book_text("books/frankenstein.txt")

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    char_count = get_num_chars(text)
    print(char_count)


main()


# Read number of words in a file
with open("books/frankenstein.txt", "r", encoding="utf-8") as file:
    content = file.read()
    words = content.split()
    word_count = len(words)

print(f"Found {word_count} total words")
