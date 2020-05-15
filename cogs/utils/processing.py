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
    return a, b


def volumeBar(count, total, bar_len=10):
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '█' * filled_len + '░' * (bar_len - filled_len)
    return '%s' % (bar)
