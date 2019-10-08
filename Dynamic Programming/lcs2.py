#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    d=[]
    for x in range(0,len(a)+1):
        d.append([])
        for y in range(0,len(b)+1):
            #print(d)
            if x==0:
                d[x].append(0)
            elif y==0:
                d[x].append(0)
            else:
                if a[x-1]==b[y-1]:
                    print(str(a[x-1])+str(x)+str(y))
                    print(b[y-1])
                    d[x].append(max(d[x-1][y],
                                    d[x][y-1],
                                    d[x-1][y-1])+1)
                else:
                    d[x].append(max(d[x-1][y],
                                    d[x][y-1],
                                    d[x-1][y-1]))
        print(d[x])
    #print(d)
    for x in d:
        print(x)
        #for y in x:
            #print()
    return d[len(a)][len(b)]

if __name__ == '__main__':
    n=int(input())
    ip=input()
    a=[int(x) for x in ip.split(" ")]
    m=int(input())
    ip=input()
    b=[int(x) for x in ip.split(" ")]
##    input = sys.stdin.read()
##    data = list(map(int, input.split()))
##
##    n = data[0]
##    data = data[1:]
##    a = data[:n]
##
##    data = data[n:]
##    m = data[0]
##    data = data[1:]
##    b = data[:m]

    print(lcs2(a, b))
