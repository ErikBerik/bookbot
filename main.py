from stats import count_words,count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    bookstring = get_book_text('books/frankenstein.txt')
    wordnumber = count_words(bookstring)
    character_counts = count_characters(bookstring)
    print(f'Found {wordnumber} total words')
    print(character_counts)

main()