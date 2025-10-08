# 快速排序
def quick_sort(arr, l, r):
    if l>=r:
        return
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
    quick_sort(arr, l, i-1)
    quick_sort(arr, i+1, r)


print("请输入要排序的数字，用空格分隔：")
arr = [int(x) for x in input().split()]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
