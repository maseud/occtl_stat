import os
import json
import subprocess

file_passwd = open('/etc/ocserv/passwd', 'r')
passwd_lines = file_passwd.readlines()
file_passwd.close()

for passwd_line in passwd_lines:
    name = passwd_line.split(":")[0].strip()
    cmd = [ "occtl", "-j", "show user", name ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    j = json.loads(output)
    print(name)
    if len(j)>0:
        j0 = j[0]
        id = j0["ID"]
        ip = j0["Remote IP"]
        rx = j0["RX"]
        tx = j0["TX"]
        datetime = j0["Connected at"]
        date  = datetime.split(" ")[0].strip()
        time  = datetime.split(" ")[1].strip()
        year  = date.split("-")[0]
        month = date.split("-")[1]
        day   = date.split("-")[2]
        duration = j0["_Connected at"].strip()
        #name = j0["Username"]
        #agent = j0["User-Agent"]
        #ses = j0["Session"]

        userdir = "users/"+year+month+"/"
        if not os.path.exists(userdir):
            os.makedirs(userdir)

        userfilename = userdir+name+".json"
        if os.path.exists(userfilename):
            file_user = open(userfilename, "r")
            stat = json.load(file_user)
            file_user.close()
        else:
            stat = {}

        index = day + time.replace(":", "")
        stat[index] = [name, rx, tx, date, time, duration, ip]
        #print stat[index]

        file_user = open(userfilename, "w")
        json.dump(stat, file_user)
        file_user.close()
