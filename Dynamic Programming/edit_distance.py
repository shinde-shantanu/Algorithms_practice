# Uses python3
def edit_distance(s, t):
    #write your code here
    d=[]
    for x in range(0,len(s)+1):
        print(x)
        d.append([])
        for y in range(0,len(t)+1):
            print(y)
            #print(d)
            if x==0:
                d[x].append([0])
            elif y==0:
                d[x].append([0])
            else:
                print(s[x-1]+t[y-1])
                if s[x-1]==t[y-1]:
                    print("a")
##                    print(str(a[x-1])+str(x)+str(y))
##                    print(b[y-1])
                    if d[x-1][y][0]>d[x][y-1][0]:
                        if d[x-1][y][0]>d[x-1][y-1][0]:
                            d[x].append([d[x-1][y][0]+1,0,1])
                        else:
                            d[x].append([d[x-1][y-1][0]+1,0,3])
                    elif d[x][y-1][0]>d[x-1][y][0]:
                        if d[x][y-1][0]>d[x-1][y-1][0]:
                            d[x].append([d[x][y-1][0]+1,0,2])
                        else:
                            d[x].append([d[x-1][y-1][0]+1,0,3])
##                    else:
##                        d[x].append([d[x-1][y-1][0]+1,0,3])
##                    d[x].append([max(d[x-1][y],
##                                    d[x][y-1],
##                                    d[x-1][y-1])+1,0,-1])
                else:
                    if d[x-1][y][0]>d[x][y-1][0]:
                        if d[x-1][y-1][0]>d[x-1][y-1][0]:
                            d[x].append([d[x-1][y][0],1,1])
                        else:
                            d[x].append([d[x-1][y-1][0],1,3])
                    elif d[x][y-1][0]>d[x-1][y][0]:
                        if d[x][y-1][0]>d[x-1][y-1][0]:
                            d[x].append([d[x][y-1][0],1,2])
                        else:
                            d[x].append([d[x-1][y-1][0],1,3])
##                    else:
##                        d[x].append([d[x-1][y-1][0],1,3])
##                    d[x].append([max(d[x-1][y],
##                                    d[x][y-1],
##                                    d[x-1][y-1]),1])
            print(d)
        print(d)
    #print(d)
    x=len(s)
    y=len(t)
    ans=0
    while x!=0:
        while y!=0:
            if(d[x][y][1]==1):
                ans+=1
            if(d[x][y][2]==1):
                x-=1
            elif(d[x][y][2]==2):
                y-=1
            else:
                x-=1
                y-=1
            #else:
                
    for x in d:
        print(x)
##        #for y in x:
##            #print()
##    return d[len(a)][len(b)]
    return ans

if __name__ == "__main__":
    print(edit_distance(input(), input()))
