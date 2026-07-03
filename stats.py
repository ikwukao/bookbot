def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    char_count = {}

    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_on(item):
    return item[1]


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []

    for char in chars_dict:
        count = chars_dict[char]
        sorted_list.append((char, count))

    sorted_list = sorted(sorted_list, key=sort_on, reverse=True)

    return sorted_list
