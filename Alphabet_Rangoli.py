# Enter your code here. Read input from STDIN. Print output to STDOUT
n,s,f = int(raw_input()),list('abcdefghijklmnopqrstuvwxyz'),[]
l,r_l = list(s[0:n]), list(reversed(s[1:n]))
middle = '-'.join(r_l+l)
for i in reversed(xrange(1,n)):
    l,r_l = list(s[i:n]), list(reversed(s[i+1:n]))
    f.append('-'.join(r_l+l).center(len(middle),'-'))
f.append(middle)
for i in xrange(1,n):
    l,r_l = list(s[i:n]), list(reversed(s[i+1:n]))
    f.append('-'.join(r_l+l).center(len(middle),'-'))
print('\n'.join(f))