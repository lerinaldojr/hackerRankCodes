# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(raw_input())
b = int(raw_input())
c = [a/b,a%b]
s = [c[0],c[1],(c[0],c[1])]
print('\n'.join(str(v) for v in s))