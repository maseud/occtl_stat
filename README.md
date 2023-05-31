# occtl_stat
OpenConnect server control (occtl) usage statistic per user per month by python 2.7

First seting a conjob to gather statistics at every minuute.

crontab -e

MAILTO=""
* * * * * python ~/setstat.py >/dev/null 2>&1

All done.

to view the statistics use getstat.py like this:

python getstat.py users/{year}{month}

example:
python getstat.py users/202306

Sample Output be like:

jack     SUM:2852518565    RX:196973224     TX:2655545341

user1    SUM:2596684216    RX:89844205      TX:2506840011

user2    SUM:2800895657    RX:218455717     TX:2582439940

john     SUM:4498438286    RX:1730360775    TX:2768077511

auser    SUM:4968223808    RX:321670091     TX:4646553717
