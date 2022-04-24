# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(raw_input())
headers = raw_input()
student = namedtuple('Student',headers)
students = []
for i in range(N):
    students.append(student(*raw_input().split()))
print sum(list(map(lambda x: float(x.MARKS),students)))/len(students)