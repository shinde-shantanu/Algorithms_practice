# Uses python3
import sys

def get_change(m):
    #write your code here
    n=0
    #print("1"+str(m))
    if(m>=10):
        #print(m)
        x=int(m/10)
        m=m-10*x
        n=n+x
        #print(m)
    if(m>=5):
        #print("a")
        x=int(m/5)
        m=m-5*x
        n=n+x
        #print(m)
    if(m>0):
        n=n+m
    return n

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
