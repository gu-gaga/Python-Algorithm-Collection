# 数组元素的目标和（双指针）
n,m,x=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
j=m-1
for i in range(n):
    while a[i]+b[j]>x:
        j-=1
    if a[i]+b[j]==x:
        print(f"{i} {j}")
        break
