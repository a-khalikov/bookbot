from stats import get_num_words
from stats import get_letter_count

def main():
    counting = get_letter_count("books/frankenstein.txt")
    for char in counting:
        print(f"'{char}': {counting[char]}")

main()




#def main():
#    num_words = get_num_words("books/frankenstein.txt")
#    print(f"{num_words} words found in the document") 
#
#main()