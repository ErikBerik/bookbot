def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(input_string):
    words = input_string.split()
    return len(words)

def main():
    bookstring = get_book_text('books/frankenstein.txt')
    wordnumber = count_words(bookstring)
    print(f'Found {wordnumber} total words')

main()