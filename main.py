from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

def main():



    text = get_book_text(path_to_book)
    num_words = count_words(text)
    num_chars = count_chars(text)
    sorted_dict = sort_dictionary(num_chars)

    print(f'{12 * "="} BOOKBOT {12 * "="}')
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"{12 * '-'} Word Count {12 * '-'}")
    print(f"Found {num_words} total words")
    print(f"{12 * '-'} Character Count {12 * '-'}")

    for dict in sorted_dict:
        print(f"{dict['char']}: {dict['count']}")
    
    print(f"{12 * '-'} END {12 * '-'}")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    f.close()


def count_words(text):
    return len(text.split())


main()
