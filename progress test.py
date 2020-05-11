import sys

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    return '[%s] %s%s ...%s\r' % (bar, percents, '%', status)

    #sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    #sys.stdout.flush()

def split_num(num):
    pos_nums = []
    c = 1
    while num != 0:
        z = num % 10
        pos_nums.append(z * c)
        num = num // 10
        c = c * 10
    return pos_nums

def mapnum(start,stop):
    stopmodifed = (stop//1000-1)*1000 
    stop -= stopmodifed
    
    startlist = split_num(start)
    start = split_num(start)[2]
    
    return start
print(mapnum(2500,3000))