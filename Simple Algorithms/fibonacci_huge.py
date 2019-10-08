# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        #c=
        previous, current = current, (previous + current) %m

    return current

if __name__ == '__main__':
    x=input()
##    for x in x.split(" ")[2]:
##        print(x)
    print(get_fibonacci_huge_naive(int(x.split(" ")[0]), int(x.split(" ")[1])))


