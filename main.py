"""
main.py

Entry point for the BookBot application.

BookBot is a command-line text analysis tool that reads a book from a
user-specified file path and generates a report containing:

    • Total word count
    • Frequency of each alphabetical character
    • Character frequencies sorted from most common to least common

Usage
-----
python3 main.py <path_to_book>

Example
-------
python3 main.py books/frankenstein.txt
"""

import sys

from stats import (
    chars_dict_to_sorted_list,
    get_num_chars,
    get_num_words,
)


def get_book_text(filepath: str) -> str:
    """
    Read and return the contents of a text file.

    Parameters
    ----------
    filepath
        Relative or absolute path to the book file.

    Returns
    -------
    str
        Complete contents of the file as a string.
    """

    with open(filepath, "r") as file:
        return file.read()


def print_report(
    book_path: str,
    word_count: int,
    sorted_chars: list[tuple[str, int]],
) -> None:
    """
    Display the formatted BookBot analysis report.

    Parameters
    ----------
    book_path
        Path of the analyzed book.

    word_count
        Total number of words found in the text.

    sorted_chars
        Character frequency data sorted in descending order.
    """

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Display only alphabetical characters.
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


def main() -> None:
    """
    Execute the BookBot application.

    The program:

    1. Validates command-line arguments.
    2. Reads the specified book.
    3. Counts the total words.
    4. Counts character frequencies.
    5. Sorts character frequencies.
    6. Prints a formatted analysis report.
    """

    # Ensure a book path was provided.
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Read the book path supplied via the command line.
    book_path = sys.argv[1]

    # Load the complete book into memory.
    text = get_book_text(book_path)

    # Calculate the total number of words.
    word_count = get_num_words(text)

    # Count occurrences of every character.
    char_count = get_num_chars(text)

    # Sort characters by frequency (highest first).
    sorted_chars = chars_dict_to_sorted_list(char_count)

    # Display the analysis report.
    print_report(
        book_path,
        word_count,
        sorted_chars,
    )


if __name__ == "__main__":
    main()
