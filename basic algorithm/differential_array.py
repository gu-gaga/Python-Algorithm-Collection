# 差分数组（前缀和的逆运算）
def insert(l,r,c):
    b[l]+=c
    b[r+1]-=c
    return 0
n,m=map(int, input().split())
a=[0]*(n+2)
b=[0]*(n+2)
i=1
for num in input().split(' '):
    insert(i,i,int(num))
    i+=1
for _ in range(m):
    l,r,c=map(int, input().split())
    insert(l,r,c)
print(b[1:n+1])
