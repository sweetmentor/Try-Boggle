def maxlist(l):
    if len(l) == 1:
        return l[0]
    
    else:
        first = l[0]
        rest = l[1:]
        max_of_rest = maxlist(rest)
        if first > max_of_rest:
            return first
        else:
            return max_of_rest
                



print(maxlist([2, 13, 5, 7, 8]))





