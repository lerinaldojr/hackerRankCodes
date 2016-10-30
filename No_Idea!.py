from collections import Counter
_,n,A,B = raw_input(), Counter(raw_input().split()), set(raw_input().split()), set(raw_input().split())
happyness = sum([n[i] for i in A]) - sum([n[i] for i in B])
print(happyness)