def next_pal(val):
    str(val)
    if str(val) != str(val)[::-1]:
        while str(val) != str(val)[::-1]:
            val += 1
    elif str(val) == str(val)[::-1]:
        while val == val:
            val += 1
        return val


print(next_pal(191))