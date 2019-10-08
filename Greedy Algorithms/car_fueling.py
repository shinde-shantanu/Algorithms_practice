# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    ans=0
    current=0
    i=0
    while(distance-current>tank):
        max=0
        while(i<len(stops)):
            if(stops[i]-current<=tank):
                max=i
                i=i+1
            else:
                break
        if(current==stops[max]):
            return -1
        current=stops[max]
        ans=ans+1
    return ans

if __name__ == '__main__':
    #d, m, _, *stops = map(int, sys.stdin.read().split())
    d=int(input())
    m=int(input())
    n=int(input())
    stops=[int(x) for x in input().split(" ")]
##    
##    for x in range(0,n):
##        stops.append(int(input()))
    print(compute_min_refills(d, m, stops))
