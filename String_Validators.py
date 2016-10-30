# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
ans = ['False']*5
for i in s:
    if i.isalpha():
        ans[0],ans[1]= 'True', 'True'
        if i.islower():
            ans[3] = 'True'
        else:
            ans[4] = 'True'
    if i.isdigit():
        ans[0],ans[2]= 'True', 'True'
        continue
print('\n'.join(ans))