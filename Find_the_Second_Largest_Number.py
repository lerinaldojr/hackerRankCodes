# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(raw_input())
b = raw_input().split(' ')
c = [int(i) for i in b]
c = sorted(set(c),reverse=True)
if(len(c)>1):
    print c[1]
else:
    print c[0]