_,s,n = raw_input(),set([int(i) for i in raw_input().split()]), int(raw_input())
for i in xrange(n):
    s_c = raw_input().split()
    if(len(s_c) == 2):
        getattr(s, s_c[0])(int(s_c[1]))
    else:
        getattr(s, s_c[0])()
print(sum(s))