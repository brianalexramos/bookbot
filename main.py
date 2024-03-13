def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_contents(book_path)
    print_book_report(book_path, contents)
        
def get_book_contents(path):
    with open(path) as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    words = text.lower()
    letter_count_dict = {}
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for char in words:
        if char in letters:
            if char in letter_count_dict:
                letter_count_dict[char] += 1
            else:
                letter_count_dict[char] = 1
    return letter_count_dict

def char_dict_to_sorted(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

def print_book_report(path, text):
    print(f"\n--- Beginning report for {path} ---\n")

    word_count = count_words(text) 
    print(f"{word_count} words found in the document\n")

    char_count = count_letters(text)
    char_count_list = char_dict_to_sorted(char_count)
    for item in char_count_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("\n--- End report ---\n")

main()