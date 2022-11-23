import string

def count_words(my_str):
    my_str = my_str.lower().split()
    ls = []
    for item in my_str:
        for char in string.punctuation:
            if char in item:
                item = item.replace(char, '')
        ls.append(item)
    my_dict = {}
    for item in ls:
        if item != '':
            my_dict[item] = ls.count(item)
    # Сортируем словарь по значению
    my_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
    return my_dict

