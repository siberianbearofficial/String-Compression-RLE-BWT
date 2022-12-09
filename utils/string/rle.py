def rle(s):
    res = ''
    i = 0
    while i < len(s):
        c = s[i]
        j = i
        while j < len(s) and s[j] == c:
            j += 1
        res += c + str(j - i)
        i = j
    return res
