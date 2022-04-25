S=raw_input()
i,c=map(str,raw_input().split())
i=int(i)
print S[:i] + c + S[i+1:]
if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new