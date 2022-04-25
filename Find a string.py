a,b=(raw_input() for i in range(2))
cnt=0
for i in range(len(a)-len(b)+1):
    if a[i:i+len(b)]==b:
        cnt+=1
print cnt
if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count