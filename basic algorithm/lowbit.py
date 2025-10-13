# 二进制中1的个数
def lowbit(x):
    return x & -x
n=int(input())
nums=list(map(int,input().split()))
a=[]
for num in nums:
    res=0
    while num:
        num-=lowbit(num)
        res+=1
    a.append(res)
print(*a)
