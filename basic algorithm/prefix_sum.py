# 求前n个数的和
n,m=map(int,input().split())
arr=list(map(int,input().split()))
S=[]
S.append(0)
for i in range(1,n+1):
    S.append(S[i-1]+arr[i-1])
for i in range(m):
    l,r=map(int,input().split())
    print(S[r]-S[l-1])