# Uses python3
import sys

def optimal_sequence(n):
    ans=[0,0,1,1]
    seq=[[0],
         [1],
         [1,2],
         [1,3]]
    c=0
    d=[2,3]
    if(n<4):
        return ans[n],seq[n]
    for x in range(4,n+1):
        #seq=[]
        #c=-1
        ans.append(x)
        seq.append([])
        #print(seq)
        for y in d:
            if y<=x:
                #print(seq)
                nc=ans[int(x/y)]+1+(x%y)
                if ans[x]>nc:
                    #print(nc)
                    ans[x]=nc
                    #print(seq[x])
                    seq[x]=[]
                    for z in seq[int(x/y)]:
                        seq[x].append(z)
                    #seq[x]=seq[int(x/y)]
                    #print(seq)
                    seq[x].append((seq[x][len(seq[x])-1])*y)
                    #seq[x].append(100)
                    #print(seq)
                    #seq[x]=t
                    #print(seq)
                    if x%y>0:
                        for z in range((x%y)):
                            t=seq[x]
                            t.append(t[len(t)-1]+1)
                            seq[x]=t
                            #print(seq)
        #print(seq)
                    #seq[c]=n*nc
##                elif ans[x]==-1:
##                    ans[x]=nc
                    #c+=1
                    #seq.append(n*nc)
    #print(ans)
    return ans[n],seq[n]
##    sequence = []
##    while n >= 1:
##        sequence.append(n)
##        if n % 3 == 0:
##            n = n // 3
##        elif n % 2 == 0:
##            n = n // 2
##        else:
##            n = n - 1
    #return reversed(sequence)

##input = sys.stdin.read()
n = int(input())
ans,sequence = optimal_sequence(n)
print(ans)
for x in sequence:
    print(x, end=' ')
