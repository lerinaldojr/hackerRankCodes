# Enter your code here. Read input from STDIN. Print output to STDOUT
x,y,z,n = int(raw_input()),int(raw_input()),int(raw_input()),int(raw_input())
print [[i,j,p] for i in xrange(x+1) for j in xrange(y+1) for p in xrange(z+1) if (i+j+p) != n]