from stats import count_words, count_characters, sort_character_counts
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_chars = sort_character_counts(char_count)
    
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print(f"--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['character']}: {entry['count']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()    
