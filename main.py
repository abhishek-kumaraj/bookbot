with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def num_of_words(book):
    words = book.split()
    return len(words)

def num_of_each_char(book):
    my_dic = {}
    book = book.lower()
    mySet = set(book)
    for element in mySet:
        countOfChar = 0
        for character in book:
            if character == element:
                countOfChar += 1
        my_dic[element] = countOfChar
    return my_dic   
      

print(num_of_each_char(file_contents))

