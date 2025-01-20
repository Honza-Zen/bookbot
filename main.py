def main():
    
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    word_count = get_words_count(text)
    char_dict = get_characters_count(text)

    print_report(book_path, word_count, char_dict)

def sort_on(dict):
    return dict["num"]

def print_report(book, word_count, char_dict):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    print("\nCharacter frequency analysis: ")
    
    char_list = []
    for key, value in char_dict.items():
        char_list.append({"name" : key, "num" : value})
        
    char_list.sort(reverse=True, key=sort_on)
    
    for char in char_list:
        if char["name"].isalpha():
            print(f"The '{char["name"]}' character was found {char["num"]} times")

    print("--- End report ---")


def get_characters_count(file_contents):
    character_dict = {}

    for char in file_contents:
        character = char.lower()
        
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    return character_dict

def get_words_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


main()