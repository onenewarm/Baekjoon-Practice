n=int(input())
stairs_score=[0 for i in range(0,301)]
for i in range(1,n+1):
    stairs_score[i]=int(input())


result=[0 for i in range(0,301)]



for i in range(1,n+1):
    if(i==1):
        result[1]=stairs_score[1]
    elif(i==2):
        result[2]=stairs_score[1]+stairs_score[2]
    else:
        result[i]=stairs_score[i]+max(stairs_score[i-1]+result[i-3],result[i-2])

print(result[n])
