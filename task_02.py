def coincidence(my_list=None, my_range=None):
    if my_list and my_range:
        my_ls = []
        for item in my_list:
            if isinstance(item, (int, float)):
                if my_range[0] <= item <= my_range[-1]:
                    my_ls.append(item)
        return my_ls
    else:
        return []
