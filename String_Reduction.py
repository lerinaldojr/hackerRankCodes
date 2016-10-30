#!/usr/bin/py
# Head ends here
def stringReduction(a):
    counts = [a.count('a'), a.count('b'), a.count('c')]
    evenOrOdd = [i%2 for i in counts].count(0)
    if(counts.count(0) > 1):
        return len(a)
    elif(evenOrOdd == 0) or (evenOrOdd == 3): 
        return 2
    return 1
# Tail starts here
if __name__ == '__main__':
    t = input()
    for i in range(0,t):
        a=raw_input()
        print stringReduction(a)