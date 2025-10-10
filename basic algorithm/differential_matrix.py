# 差分矩阵（二维差分数组）
import numpy as np
def insert(x1,y1,x2,y2,c):
    b[x1][y1]+=c
    b[x2+1][y1]-=c
    b[x1][y2+1]-=c
    b[x2+1][y2+1]+=c
    return 0
n,m,q=map(int,input().split())
a=np.zeros((n+2,m+2),dtype=int)
b=np.zeros((n+2,m+2),dtype=int)
for i in range(1,n+1):
    for j,num in enumerate(input().split(' '),1):
        insert(i,j,i,j,int(num))
for _ in range(q):
    x1,y1,x2,y2,c=map(int,input().split())
    insert(x1,y1,x2,y2,c)
for i in range(1,n+1):
    for j in range(1,m+1):
        a[i][j]=a[i-1][j]+a[i][j-1]-a[i-1][j-1]+b[i][j]
print(a[1:n+1,1:m+1])
