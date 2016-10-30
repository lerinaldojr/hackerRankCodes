# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
s_m = [a.upper() if a.islower() else a.lower() for a in s ]
print(''.join(s_m))