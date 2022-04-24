from collections import defaultdict
d = defaultdict(list)
n,m = map(int, raw_input().split())
for i in range(1,n+1):
    d[raw_input()].append(str(i))

for _ in range(m):
    w = raw_input()
    if w in d:
        print " ".join(d[w])
    else:
        print -1