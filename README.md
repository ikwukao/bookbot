# 📚 BookBot

BookBot is a command-line Python application that analyzes the contents of a text file and generates a readable report containing:

* Total number of words
* Frequency of every alphabetical character
* Characters sorted from most common to least common

This project was built as part of the **Boot.dev Backend Developer Path** to practice Python fundamentals, file handling, dictionaries, functions, sorting, and command-line arguments.

---

## Features

* Reads any plain text (`.txt`) book.
* Counts the total number of words.
* Counts occurrences of every character (case-insensitive).
* Filters non-alphabetical characters from the final report.
* Sorts character frequencies in descending order.
* Accepts the book path as a command-line argument.

---

## Project Structure

```text
bookbot/
├── books/
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
├── main.py
├── stats.py
└── README.md
```

---

## Requirements

* Python 3.10 or later

Verify your Python installation:

```bash
python3 --version
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ikwukao/bookbot.git
```

Navigate into the project directory:

```bash
cd bookbot
```

---

## Usage

Run the program by providing the path to a text file:

```bash
python3 main.py books/frankenstein.txt
```

You can analyze any supported text file:

```bash
python3 main.py books/mobydick.txt
```

```bash
python3 main.py books/prideandprejudice.txt
```

---

## Example Output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
...
============= END ===============
```

---

## How It Works

1. Reads the specified text file.
2. Counts the total number of words.
3. Counts every character (case-insensitive).
4. Converts the character dictionary into a sorted list.
5. Prints a formatted analysis report.

---

## Technologies Used

* Python 3
* File I/O
* Dictionaries
* Lists and Tuples
* Functions
* Sorting with custom keys
* Command-Line Interface (CLI)

---

## Learning Objectives

This project demonstrates understanding of:

* Python functions
* Modular programming
* Reading files
* String manipulation
* Dictionaries
* Sorting collections
* Command-line arguments (`sys.argv`)
* Clean code organization

---

## Future Improvements

Possible enhancements include:

* Support for multiple file formats
* Analysis of multiple books in one command
* Most common word analysis
* Sentence and paragraph statistics
* CSV or JSON report export
* Graphical visualizations
* Stop-word filtering
* Reading level metrics

---

## License

This project is provided for educational purposes.

The sample books used for testing are available from Project Gutenberg and remain subject to their respective licensing terms.

---

## Acknowledgements

* Boot.dev Backend Developer Path
* Project Gutenberg for providing free public-domain books
* Python Software Foundation
