# Enter your code here. Read input from STDIN. Print output to STDOUT
s = list(raw_input())
vs = raw_input().split(' ')
index,ch = int(vs[0]), vs[1]
s[index] = ch 
print(''.join(s))