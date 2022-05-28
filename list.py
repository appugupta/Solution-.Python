# Enter your code here. Read input from STDIN. Print output to STDOUT
L = []
lines = int(input())
for i in range(lines):
    line = input().split()
    command = line[0]
    if command == 'append':
        L.append(int(line[1]))
    elif command == 'insert':
        L.insert(int(line[1]), int(line[2]))
    elif command == 'remove':
        L.remove(int(line[1]))
    elif command == 'print':
        print(L)
    elif command == 'sort':
        L.sort()
    elif command == 'pop':
        L.pop()
    elif command == 'reverse':
        L.reverse()
    elif command == 'count':
        L.count(int(line[1]))