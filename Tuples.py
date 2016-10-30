# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
print(hash(tuple([int(i) for i in raw_input().split()])))
