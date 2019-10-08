# Uses python3
def calc_fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        a=0
        b=1
        for x in range(2,n+1):
            c=a+b
            a=b
            b=c
#            print(b)
        return b

n = int(input())
print(calc_fib(n)%10)
##for x in range(2,20):
##    print(x)
