# 差分数组（前缀和的逆运算）
def insert(l,r,c):
    b[l]+=c
    b[r+1]-=c
    return 0
n,m=map(int,input().split())
a=[0]*(n+2)
b=[0]*(n+2)
for i,num in enumerate(input().split(' '),1):
    insert(i,i,int(num))
for _ in range(m):
    l,r,c=map(int, input().split())
    insert(l,r,c)
for i in range(1,n+1):
    a[i]=a[i-1]+b[i]
print(a[1:n+1])
