import os
import sys
import json

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', ' KB', ' MB', ' GB', ' TB'][magnitude])

if len(sys.argv)<2:
    print("Usage: python getstat.py filename")
    raise SystemExit

# Iterate directory
filenames = []
dir_path = sys.argv[1]
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        filenames.append(path)
#print(filenames)

all = []
sumrx = 0
sumtx = 0
for filename in filenames:
    userfilename = os.path.join(dir_path, filename)
    file_user = open(userfilename, "r")
    stats = json.load(file_user)
    file_user.close()
    #print(stats)
    #stat[index] = [name, rx, tx, date, time, duration, ip]

    rx = 0
    tx = 0
    for stat in stats.values():
        name = stat[0]
        rx = rx + int(stat[1])
        tx = tx + int(stat[2])

    sumrx = sumrx + rx
    sumtx = sumtx + tx
    all.append([rx+tx, name, rx, tx])

all.sort()
for item in all:
    if len(item[1])<8:
        print item[1] + "\t\tSUM:" + str(item[0]) + "\t\tRX:" + str(item[2]) + "\t\tTX:" + str(item[3])
    else:
        print item[1] + "\tSUM:" + str(item[0]) + "\t\tRX:" + str(item[2]) + "\t\tTX:" + str(item[3])
print "------------\t------------\t\t------------\t\t------------"
print "TOTAL\t\tSUM:"+human_format(sumrx+sumtx)+"\t\tRX:"+human_format(sumrx)+"\t\tTX:"+human_format(sumtx)
