# 区间和
n,m=map(int,input().split())
reflect={}
ls=[]
rs=[]
for _ in range(n):
    x,c=map(int,input().split())
    reflect[x]=reflect.get(x,0)+c
for _ in range(m):
    l,r=map(int,input().split())
    ls.append(l)
    rs.append(r)
    reflect[l]=reflect.get(l,0)
    reflect[r]=reflect.get(r,0)
sorted_keys=sorted(reflect)
index={key:idx for idx,key in enumerate(sorted_keys)}
s=[0]*(len(sorted_keys)+1)
for i in range(len(sorted_keys)):
    s[i+1]=(s[i]+reflect[sorted_keys[i]])
for i in range(m):
    print(s[index[rs[i]]+1]-s[index[ls[i]]])
