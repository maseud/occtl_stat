import os
import sys
import json

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
print(filenames)

all = []
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
    sum = rx + tx
    all.append([sum, name, rx, tx])

all.sort()
for item in all:
    print item[1] + "\t\tSUM:" + str(item[0]) + "\t\tRX:" + str(item[2]) + "\t\tTX:" + str(item[3])