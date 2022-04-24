# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime, timedelta

def gettime():
    s = raw_input()
    t = datetime.strptime(s[:-6], "%a %d %b %Y %H:%M:%S")
    m = int(s[-2:])  
    h = int(s[-4:-2])
    if s[-5] == '+':
        t -= timedelta(hours=h, minutes=m)
    else:
        t += timedelta(hours=h, minutes=m)
    return t
for _ in xrange(input()):
    t1 = gettime()
    t2 = gettime()
    d = abs(t1 - t2)
    #print d
    print d.days * 86400 + d.seconds