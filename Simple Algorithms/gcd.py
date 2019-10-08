# Uses python3
import sys

def gcd_naive(a, b):
    if(b==0):
        return a
    else:
        return(gcd_naive(b,a%b))

if __name__ == "__main__":
    x=input()
##    for x in x.split(" ")[2]:
##        print(x)
    print(gcd_naive(int(x.split(" ")[0]), int(x.split(" ")[1])))
