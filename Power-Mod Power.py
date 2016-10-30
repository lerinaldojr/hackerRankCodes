# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(raw_input())
b = int(raw_input())
m = int(raw_input())
c = [str(pow(a,b)), str(pow(a,b,m))]
print('\n'.join(c))