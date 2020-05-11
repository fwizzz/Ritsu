def split_num(num):
    pos_nums = []
    c = 1
    while num != 0:
        z = num % 10
        pos_nums.append(z * c)
        num = num // 10
        c = c * 10
    return pos_nums


def mapnum(a, b):
    stopmodifed = (b // 1000 - 1) * 1000
    b -= stopmodifed
    if len(split_num(a)) > 2:
       a = split_num(a)[2]
    else:
       pass
    return a,b



print(split_num(40))