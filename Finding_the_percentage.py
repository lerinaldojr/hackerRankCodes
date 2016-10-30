# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
d = {}
for l in xrange(n+1):
    j = raw_input().split(' ')
    if j[0] in d:
        print('%.2f'%d[j[0]])
    else:
        d[j[0]] = sum([float(i) for i in j[1:]])/len(j[1:])