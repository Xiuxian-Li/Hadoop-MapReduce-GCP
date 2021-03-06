import sys


def process_temperature():
    for line in sys.stdin:
        line = line.strip()

        date = int(line[15:23])
        temperature = int(line[87:92])
        quality = int(line[92:93])

        if temperature != '+9999' or quality in quality_list:
            print('%s\t%s' % (date, temperature))


quality_list = ['0', '1', '4', '5', '9']
process_temperature()
