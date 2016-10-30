# Enter your code here. Read input from STDIN. Print output to STDOUT
n,lista = int(raw_input()),[]
for i in xrange(n):
    command = raw_input()
    if command == 'print':
        print lista
    else:
        s_c = command.split()
        if(len(s_c) > 2):
            getattr(lista, s_c[0])(int(s_c[1]),int(s_c[2]))
        elif(len(s_c) == 2):
            getattr(lista, s_c[0])(int(s_c[1]))
        else:
            getattr(lista, s_c[0])()