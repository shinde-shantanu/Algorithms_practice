### Uses python3
##import sys
##
##def get_fibonacci_last_digit_naive(n):
##    if n <= 1:
##        return n
##
##    previous = 0
##    current  = 1
##
##    for _ in range(n - 1):
##        previous, current = current, previous + current
##        
##    return current
##
##if __name__ == '__main__':
##    input = sys.stdin.read()
##    n = int(input)
##    print(get_fibonacci_last_digit_naive(n))
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
            b=c%10
#            print(b)
        return b

n = int(input())
print(calc_fib(n))
##for x in range(2,20):
##    print(x)
