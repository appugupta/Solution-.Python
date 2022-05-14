n=int(raw_input())
my=set(map(int,raw_input().split()))
m=int(raw_input())
my2=set(map(int,raw_input().split()))
for i in sorted(my.union(my2)):
	if i not in my.intersection(my2):
		print i