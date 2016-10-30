# Enter your code here. Read input from STDIN. Print output to STDOUT
s, sub, match,v = raw_input(),raw_input(),0,0
v = s.find(sub,v)
while v > -1 :
    match+=1
    v = s.find(sub,v+1)
print(match)