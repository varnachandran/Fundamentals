
"""Implement an algorithm to determine if a string has all unique characters
 What if you can not use additional data structures?"""


def does_contain_all_unique_characters(string):
    char_set = [False] * 256

    for letter in string:
        ascii_value = ord(letter)
        if char_set[ascii_value]:
            return False
        char_set[ascii_value] = True
    return True


print(does_contain_all_unique_characters('manu'))


def check_unique_letter(string):
    checker=0 
    for letter in string:
        value=ord(letter) - ord('A')
        shiftedvalue=1<<value
        checkcondition=checker&shiftedvalue
        if checkcondition > 0:
            return False
        checker= checker | shiftedvalue
    return True

print(check_unique_letter('Varna'))
