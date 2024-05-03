def main():
    file_path='books/frankenstein.txt'

    file_contents = open_book_file(file_path)

    word_count = count_words(file_contents)

    lcd = count_letters(file_contents)
    lcd_list = sort_dictionary(lcd)

    output_report(file_path, word_count, lcd_list)

def open_book_file(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_letters(file_contents):
    letter_count_dictionary = {}
    lowercase_contents = file_contents.lower()
    for letter in lowercase_contents:
        if letter.isalpha():
            if letter not in letter_count_dictionary:
                letter_count_dictionary[letter] = 0
            letter_count_dictionary[letter] += 1
    
    return letter_count_dictionary

#lcd letter_count_dictionary
def sort_dictionary(lcd):
    lcd_list = []
    for x in lcd:
        temp = {'letter':x,'num':lcd[x]}
        lcd_list.append(temp)

    lcd_list.sort(reverse=True, key=sort_on)
    return lcd_list

def sort_on(dict):
    return dict["num"]

def output_report(file_path, word_count, lcd_list):
    print(f"--- Begin report of {file_path}  ---")
    print(word_count , " words found in this document")
    for item in lcd_list:
        print(f"The '{item['letter']}' letter was found {item['num']} times." )

    print(f"--- End Report of {file_path} ---")

main()