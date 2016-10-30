# Enter your code here. Read input from STDIN. Print output to STDOUT
n,v = raw_input(), [int(i) for i in raw_input().split()]
s_v = set(v)
print(sum(s_v)/float(len(s_v)))