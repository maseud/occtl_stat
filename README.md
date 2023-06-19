# occtl_stat
OpenConnect server control (occtl) usage statistic per user per month by python 2.7

First seting a conjob to gather statistics at every minuute.

crontab -e

MAILTO=""
* * * * * python ~/setstat.py >/dev/null 2>&1

All done.

to view the statistics use getstat.py like this:

python getstat.py users/{year}{month} [filter]

example:
python getstat.py users/202306

Sample Output be like:

user3           SUM:2.48 GB     RX:159 MB       TX:2.32 GB

user11          SUM:3.2 GB      RX:2.12 GB      TX:1.08 GB

user6           SUM:4.22 GB     RX:226 MB       TX:4 GB

user2           SUM:5.14 GB     RX:1.88 GB      TX:3.25 GB

user12          SUM:5.18 GB     RX:298 MB       TX:4.88 GB

user5           SUM:10.7 GB     RX:302 MB       TX:10.4 GB

user10          SUM:11.3 GB     RX:533 MB       TX:10.8 GB

user7           SUM:13 GB       RX:655 MB       TX:12.3 GB

user9           SUM:18.4 GB     RX:490 MB       TX:17.9 GB

user            SUM:19.1 GB     RX:1.39 GB      TX:17.7 GB

user13          SUM:20.9 GB     RX:1.36 GB      TX:19.5 GB

user4           SUM:26.6 GB     RX:5.72 GB      TX:20.9 GB

user8           SUM:26.7 GB     RX:2.58 GB      TX:24.1 GB

------------    ------------    ------------    ------------

TOTAL           SUM:167 GB      RX:17.7 GB      TX:149 GB
