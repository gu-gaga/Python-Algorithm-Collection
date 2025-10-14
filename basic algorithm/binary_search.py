# 用二分查找确定数的范围
def check_mid(arr,num,n):
    l,r=0,n-1
    while l<r:
        mid=(l+r)//2
        if arr[mid]>=num:
            r=mid
        else:
            l=mid+1
    if arr[l]!=num:
        print("-1 -1")
    else:
        while r+1<n and arr[r+1]==num:
            r+=1
        print(f"{l} {r}")
    return 0

n,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(q):
    check_mid(arr,int(input()),n)
