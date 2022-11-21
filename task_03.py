def max_odd(my_list):
    my_list = [i for i in my_list if isinstance(i, int | float) and i % 2 == 1]
    try:
        return int(max(my_list))
    except ValueError:
        return None
