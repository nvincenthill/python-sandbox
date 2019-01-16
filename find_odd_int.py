def find_odd_int(seq):
    tally = {}
    for i in seq:
        if i in tally:
            tally[i] = not tally[i]
        else:
            tally[i] = True
    for j in tally:
        if tally[j]:
            return j


print(find_odd_int([1, 2, 3, 1, 2]))
