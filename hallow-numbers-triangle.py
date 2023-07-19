n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if(j==1 or i==n or j==i):
            print(j,end="")
        else:
            print(" ",end="")
    print()
