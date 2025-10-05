from stats import count_words,count_characters,sorted_list_of_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():

    arguments = sys.argv
    if len(arguments)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookpath = arguments[1]

    bookstring = get_book_text(bookpath)
    wordnumber = count_words(bookstring)
    character_counts = count_characters(bookstring)
    character_dicts = sorted_list_of_dicts(character_counts) 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f'Found {wordnumber} total words')
    print("--------- Character Count -------")
    for item in character_dicts:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")


main()