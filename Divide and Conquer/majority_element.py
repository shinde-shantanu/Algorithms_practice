# Uses python3
import sys

##def msort(a):
###    print(a)
##    if(len(a)==1):
##        #print("a")
##        return a
##    else:
##        m=int(len(a)/2)
##        left=msort(a[0:m])
##        #print("a")
##        #print(a[m:len(a)-1])
##        right=msort(a[m:len(a)])
####        print("left"+str(left))
####        print("right"+str(right))
##        l=0
##        r=0
##        ans=[]
##        for x in range(0,len(a)):
##            if(l==len(left)):
##                ans.append(right[r])
##                r=r+1
##            elif(r==len(right)):
##                ans.append(left[l])
##                l=l+1
##            elif(left[l]<=right[r]):
##                ans.append(left[l])
##                l=l+1
##            else:
##                ans.append(right[r])
##                r=r+1
##        #print("ans"+str(ans))
##        return ans

def get_majority_element(a, left, right):
##    a=msort(a)
##    c=a[0]
##    count=1
##    for x in range(1,len(a)-1):
####        print(count)
####        print(a[x])
##        if(a[x]!=c):
###            print(len(a)/2)
##            if(count>(len(a)/2)):
##                return 1
##            else:
##                count=1
##                c=a[x]
##        else:
##            count=count+1
##    return -1
        #print(count)
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

if __name__ == '__main__':
    n=int(input())
    ip=input()
    a=[int(x) for x in ip.split(" ")]
##    input = sys.stdin.read()
##    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
