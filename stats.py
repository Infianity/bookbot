def count_words(text):
    return len(text.split())

def count_characters(text):
    """Returns a dictionary with the count of each character in the text """
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char,0) + 1
    return char_count

def sort_character_counts(char_count):
    sorted_chars = [
        {"character": char, "count": count}
        for char, count in char_count.items() if char.isalpha()
    ]
    sorted_chars.sort(key=lambda x: x["count"], reverse=True)
    return sorted_chars

