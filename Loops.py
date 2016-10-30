# Enter your code here. Read input from STDIN. Print output to STDOUT
i = int(raw_input())
print('\n'.join([str(pow(j,2)) for j in xrange(i)]))