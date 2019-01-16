def find_odd_int(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


# print(find_odd_int([1, 2, 3, 1, 2]))
