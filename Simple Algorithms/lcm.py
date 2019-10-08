# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, max(a,b)+1):
        if (min(a,b)*l)%max(a,b)==0:
            return l*min(a,b)

    return a*b

if __name__ == '__main__':
    x=input()
##    for x in x.split(" ")[2]:
##        print(x)
    print(lcm_naive(int(x.split(" ")[0]), int(x.split(" ")[1])))


