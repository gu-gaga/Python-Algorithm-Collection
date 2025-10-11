# 判断一个序列是否为另一个序列的子序列
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=0
for j in range(m):
    if a[i]==b[j]:
        i+=1
    if i==n-1:
        print("Yes")
        break
if i!=n-1:
    print("No")
