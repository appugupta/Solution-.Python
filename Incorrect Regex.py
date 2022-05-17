import re

for t in xrange(int(input())):
    S = raw_input()
    try:
        re.compile(S)
        print True
    except:
        print False