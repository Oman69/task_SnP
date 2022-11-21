import string

def clear_string(stroka):
    new_str = ''
    for char in str(stroka):
        if char not in string.punctuation and char != ' ':
            new_str += char.lower()
    print(new_str)
    return new_str


def is_palindrome(string):
    string = clear_string(string)
    return string == string[::-1]

