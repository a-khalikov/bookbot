import sys
from stats import get_num_words
from stats import sort_char

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    sorting = sort_char(file_path)

    print("----------- Word Count ----------")
    num_words = get_num_words(file_path)
    print(f"Found {num_words} total words") 

    print("--------- Character Count -------")
    for char, count in sorting:
        print(f"{char}: {count}")
    
    print("============= END ===============")

main()