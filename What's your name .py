def full_name(f,s):
    return 'Hello %s %s! You just delved into python.' % (f,s)

first = raw_input()
second = raw_input()
    
print full_name(first, second)
if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)