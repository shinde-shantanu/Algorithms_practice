# Uses python3
import sys

def get_change(m):
    #write your code here
    d=[1,3,4]
    ans=[0]
    for x in range(1,m+1):
        ans.append(-1)
        for y in d:
            if(y<=x):
                nc=ans[x-y]+1
                if nc<ans[x]:
                    ans[x]=nc
                elif ans[x]==-1:
                    ans[x]=nc
    return ans[m]

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
