# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
w = len(bin(N)[1:])
print('\n'.join(['%*s'%(w-1,i)+'%*s'%(w,oct(i)[1:])+'%*s'%(w,(hex(i)[2:]).upper())+'%*s'%(w,bin(i)[2:]) for i in xrange(1,N+1)]))