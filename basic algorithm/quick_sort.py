# 快速排序
def quick_sort(arr, l, r):
    if l >= r:
        return
    pivot = arr[(l + r) // 2]
    i, j = l, r
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if l < j:
        quick_sort(arr, l, j)
    if i < r:
        quick_sort(arr, i, r)

n=int(input())
arr=list(map(int,input().split()))
quick_sort(arr,0,n-1)
print(*arr)
