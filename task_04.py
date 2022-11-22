def sort_list(my_list=None):
    if my_list:
        new_ls = []
        for item in my_list:
            if item == min(my_list):
                new_ls.append(max(my_list))
            elif item == max(my_list):
                new_ls.append(min(my_list))
            else:
                new_ls.append(item)
        new_ls.append(min(my_list))
        return new_ls
    else:
        return []
