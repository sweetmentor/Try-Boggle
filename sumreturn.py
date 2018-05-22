def sumlist(l):
    if l == []:
        return 0
    else:
        first = l[0]
        rest = l[1:]
        return first + sumlist(rest)

    
print(sumlist([1, 4, 13, 34, 56]))


