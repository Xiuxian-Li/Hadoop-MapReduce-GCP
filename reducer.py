import sys


def find_max_temp(target_date, target_temp):
    for line in sys.stdin:
        line = line.strip()
        date, temperature = line.split('\t', 1)
        try:
            temperature = int(temperature)
        except ValueError:
            continue

        if target_date == date:
            target_temp = max(target_temp, temperature)
        else:
            if target_date:
                print('%s\t%d' % (target_date, target_temp))
            target_date = date
            target_temp = temperature

    return target_date, target_temp


find_date = None
res_date, res_temp = find_max_temp(None, -float("inf"))
if res_date == find_date:
    print('%s\t%d' % (res_date, res_temp))
