# Enter your code here. Read input from STDIN. Print output to STDOUT
n,d = int(raw_input()),{}
for i in xrange(n):
    nome,nota = raw_input(),float(raw_input())
    if nota in d:
        d[nota].append(nome)
    else:
        d[nota] = [nome]
keys = sorted(d.keys())
print('\n'.join(sorted(d[keys[1]])))