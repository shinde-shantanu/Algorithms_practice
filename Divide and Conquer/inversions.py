# Uses python3
import sys

def get_number_of_inversions(a):
#    print(a)
    number_of_inversions = 0
    if len(a)==1:
        return number_of_inversions,a
    ave = int(len(a)/2)
    x1,left= get_number_of_inversions(a[0:ave])
    x2,right= get_number_of_inversions(a[ave:len(a)])
    #write your code here
    l=0
    r=0
    ans=[]
    for x in range(0,len(a)):
        if(l==len(left)):
            ans.append(right[r])
            r=r+1
        elif(r==len(right)):
            #number_of_inversions +=1
            ans.append(left[l])
            l=l+1
        elif(left[l]<=right[r]):
            ans.append(left[l])
            l=l+1
        else:
            number_of_inversions +=len(left)-l
            ans.append(right[r])
            r=r+1
    number_of_inversions +=x1+x2
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
#    print(number_of_inversions)
    return number_of_inversions,ans

if __name__ == '__main__':
    n=int(input())
    ip=input()
    a=[int(x) for x in ip.split(" ")]
##    input = sys.stdin.read()
##    n, *a = list(map(int, input.split()))
    #b = n * [0]
    ans,a=get_number_of_inversions(a)
    print(ans)
