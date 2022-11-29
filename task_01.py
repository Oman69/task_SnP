import string


def clear_string(my_str):
    new_str = ''
    for char in str(my_str):
        if char not in string.punctuation and char != ' ':
            new_str += char.lower()
    print(new_str)
    return new_str


def is_palindrome(my_str):
    my_str = clear_string(my_str)
    return my_str == my_str[::-1]

