"""
stats.py

Provides text analysis utilities for the BookBot application.

This module contains helper functions for analyzing text, including:

    • Counting the total number of words.
    • Counting the frequency of every character.
    • Sorting character frequencies from highest to lowest.

These functions are used by BookBot to generate its final analysis report.
"""


def get_num_words(text: str) -> int:
    """
    Count the total number of words in a text.

    Words are determined by splitting the text on whitespace.

    Parameters
    ----------
    text
        Text to analyze.

    Returns
    -------
    int
        Total number of words.
    """

    words = text.split()
    return len(words)


def get_num_chars(text: str) -> dict[str, int]:
    """
    Count the occurrences of every character in a text.

    All characters are converted to lowercase before counting so that
    uppercase and lowercase letters are treated as the same character.

    Parameters
    ----------
    text
        Text to analyze.

    Returns
    -------
    dict[str, int]
        Dictionary mapping each character to its frequency.
    """

    char_count: dict[str, int] = {}

    # Count each character in the text.
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_on(item: tuple[str, int]) -> int:
    """
    Return the count portion of a character-count tuple.

    This helper function is used as the sorting key when ordering
    character frequencies.

    Parameters
    ----------
    item
        A tuple containing a character and its count.

    Returns
    -------
    int
        The character's frequency.
    """

    return item[1]


def chars_dict_to_sorted_list(
    chars_dict: dict[str, int],
) -> list[tuple[str, int]]:
    """
    Convert a character frequency dictionary into a sorted list.

    The returned list is sorted in descending order based on the
    frequency of each character.

    Parameters
    ----------
    chars_dict
        Dictionary of character frequencies.

    Returns
    -------
    list[tuple[str, int]]
        List of (character, count) tuples sorted from highest to
        lowest frequency.
    """

    sorted_list: list[tuple[str, int]] = []

    # Convert the dictionary into a list of tuples.
    for char in chars_dict:
        count = chars_dict[char]
        sorted_list.append((char, count))

    # Sort by frequency in descending order.
    sorted_list = sorted(
        sorted_list,
        key=sort_on,
        reverse=True,
    )

    return sorted_list
