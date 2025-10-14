# 快速选择
def quick_sort(arr, l, r,k):
    if l==r:
        return arr[l]
    mid = arr[l]
    i,j=l,r
    while i < j:
        while i < j and arr[j]>mid:
            j-=1
        if i<j:
            arr[i]=arr[j]
            i+=1
        while i < j and arr[i]<=mid:
            i+=1
        if i<j:
            arr[j]=arr[i]
            j-=1
    arr[i]=mid
    if k-1==i:
        return arr[i]
    elif k-1<i:
        return quick_sort(arr, l, i-1,k)
    else:
        return quick_sort(arr, i+1, r,k)

n,k=map(int,input().split())
arr=list(map(int,input().split()))
print(quick_sort(arr, 0, n-1, k))
