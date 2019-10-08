# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    while(capacity>0):
        max=0
        for x in range(0,len(weights)):
            #print(x)
            #print(values[x]/weights[x])
            if((values[max]/weights[max])<(values[x]/weights[x])):
                max=x
                #print(x)
        #print(weights[max])
        a=min(capacity,weights[max])
        value=value+a*values[max]/weights[max]
        values[max]=0
        capacity=capacity-a
    return value


if __name__ == "__main__":
    ip=input()
    n=int(ip.split(" " )[0])
    capacity=int(ip.split(" " )[1])
    weights=[]
    values=[]
    for x in range(0,n):
        ip=input()
        weights.append(int(ip.split(" ")[1]))
        values.append(int(ip.split(" ")[0]))
##    data = list(map(int, sys.stdin.read().split()))
##    n, capacity = data[0:2]
##    values = data[2:(2 * n + 2):2]
##    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
