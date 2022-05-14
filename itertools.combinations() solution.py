from itertools import combinations

S,k = raw_input().split()
k = int(k)

for r in xrange(1,k+1):
    print '\n'.join(sorted(''.join(sorted(c)) for c in combinations(S,r)))