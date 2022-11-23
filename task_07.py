def combine_anagrams(input_array):
    matrix = []
    for i in input_array:
        row = []
        for j in input_array:
            if sorted(list(i.lower())) == sorted(list(j.lower())):
                row.append(j)
        if row not in matrix:
            matrix.append(row)
    return matrix

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
print(combine_anagrams(["топот", "потоп", "potatoes", "racs", "four", "scar", "creams", "scream"]))