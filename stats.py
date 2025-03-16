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
    
def main():
    counting = get_letter_count("books/frankenstein.txt")
    for char in counting:
        print(f"'{char}': {counting[char]}")

main()