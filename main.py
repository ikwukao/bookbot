def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()


# Count number of words
with open("books/frankenstein.txt", "r", encoding="utf-8") as file:
    content = file.read()
    words = content.split()
    word_count = len(words)

    print(f"Found {word_count} total words")
