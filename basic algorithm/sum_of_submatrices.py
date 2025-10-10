# 子矩阵的和（二维前缀和）
import numpy as np
n,m,q=map(int,input().split())
matrix=np.zeros((n+1,m+1),dtype=int)
S=np.zeros((n+1,m+1),dtype=int)
print(S)
for i in range(1,n+1):
    matrix[i][1:] = list(map(int,input().split()))
for i in range(1,n+1):
    for j in range(1,m+1):
        S[i][j]=S[i-1][j]+S[i][j-1]-S[i-1][j-1]+matrix[i][j]
for i in range(q):
    x1,y1,x2,y2=map(int,input().split())
    print(S[x2][y2]-S[x1-1][y2]-S[x2][y1-1]+S[x1-1][y1-1])
