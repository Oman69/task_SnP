def connect_dicts(dict1, dict2):
    new_dict = {}
    if sum(dict1.values()) > sum(dict2.values()):
        for key, value in dict2.items():
            if value > 9:
                new_dict[key] = value
        for key, value in dict1.items():
            if value > 9:
                new_dict[key] = value
    else:
        for key, value in dict1.items():
            if value > 9:
                new_dict[key] = value
        for key, value in dict2.items():
            if value > 9:
                new_dict[key] = value

    new_dict = dict(sorted(new_dict.items(), key=lambda x: x[1]))
    return new_dict
