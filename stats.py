def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        word_split = file_contents.split()
        word_count = len(word_split)
    return word_count

def get_letter_count(file_path):
    char_count = {}
    with open(file_path) as f:
        file_contents = f.read()
        lower_case = file_contents.lower()
        for char in lower_case:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count

def sort_char(file_path):
    char_count = get_letter_count(file_path)
    alpha_char = {char: count for char, count in char_count.items() if char.isalpha()}
    sorted_char = list(alpha_char.items())
    sorted_char.sort(key=lambda item: item[1], reverse=True)
    return sorted_char