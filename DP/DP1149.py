def DP(n):
    d=[[0]*3 for i in range(n)]
    for i in range(n):
        user_input=list(map(int,input().split(" ")))
        d[i]=user_input
    result = [[0]*3 for i in range(n)]
    for i in range(0,n):
        if (i==0):
            result[i]=d[i]
        else:
            result[i][0]=d[i][0]+min(result[i-1][1],result[i-1][2])
            result[i][1]=d[i][1]+min(result[i-1][0],result[i-1][2])
            result[i][2]=d[i][2]+min(result[i-1][0],result[i-1][1])
    return min(result[n-1][0],result[n-1][1],result[n-1][2])
x=int(input())
print(DP(x))
