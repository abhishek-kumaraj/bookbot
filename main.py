with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def num_of_words(book):
    words = book.split()
    return len(words)

print(num_of_words(file_contents))

