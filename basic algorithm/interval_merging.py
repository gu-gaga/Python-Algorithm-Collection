# 区间和
n=int(input())
a=[]
for i in range(n):
    l,r=map(int,input().split())
    a.append([l,r])
a=sorted(a)
num=n
st=a[0][0]
ed=a[0][1]
for i in range(n-1):
    if a[i+1][1]<=ed:
        num-=1
        continue
    else:
        if a[i+1][0]<=ed:
            num-=1
        else:
            st=a[i+1][0]
        ed=a[i+1][1]
print(num)
