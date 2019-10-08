# Uses python3
import sys

def binary_search(a, x,l,r):
    if(r<l):
        return -1
    else:
        m=int(l+((r-l)/2))
        if(a[m]==x):
            return(m)
        elif(x<a[m]):
            return binary_search(a,x,l,m-1)
        else:
            return binary_search(a,x,m+1,r)
##    #left, right = 0, len(a)
####    print(left,end=' ')
####    print(right)
##    # write your code here
##    #print("a")
##    print(str(l)+"a"+str(r))
##    if(l==r):
##        if(a[l]==x):
##            return l
##        else:
##            return -1
##    if(r<l):
##        return(-1)
##    m=int((r-l)/2)
##    if(x==a[m]):
##        return m
####    elif(left==right):
####        return -1
##    else:
##        return(max(binary_search(a,x,l,m-1),binary_search(a,x,m+1,r)))

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    ip = input()
    ip = ip.split(" ")
    n = int(ip[0])
    a = [int(x) for x in ip[1:n+1]]
    ip = input()
    #print(n)
    ip = ip.split(" ")
    k = int(ip[0])
    b = [int(x) for x in ip[1:k+1]]
    #print(a)
    for x in b:
        print(binary_search(a,x,0,n-1),end=' ')
##    input = sys.stdin.read()
##    data = list(map(int, input.split()))
##    n = data[0]
##    m = data[n + 1]
##    a = data[1 : n + 1]
##    for x in data[n + 2:]:
##        # replace with the call to binary_search when implemented
##        print(linear_search(a, x), end = ' ')
