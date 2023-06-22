def main():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words(file_contents)} words found in the document")

    my_dic = num_of_each_char(file_contents)
    my_list = sorted(my_dic.items(), key=lambda x: x[1], reverse=True)
    orted_keys = [item[0] for item in my_list]
    for item in orted_keys:
        print(f"The '{item}' character was found {my_dic[item]} times")
    print("--- End report ---")

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
        if element.isalpha():
            countOfChar = 0
            for character in book:
                if character == element:
                   countOfChar += 1
            my_dic[element] = countOfChar
        
    return my_dic   
    

main()
