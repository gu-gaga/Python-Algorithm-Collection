# 归并排序
def merge_sort(arr,l,r):
    if l>=r:
        return
    mid=(l+r)//2
    merge_sort(arr,l,mid)
    merge_sort(arr,mid+1,r)

    temp=[]
    i,j=l,mid+1
    while i<=mid and j<=r:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j += 1
    while i<=mid:
        temp.append(arr[i])
        i+=1
    while j<=r:
        temp.append(arr[j])
        j+=1

    for a in range(len(temp)):
        arr[l+a]=temp[a]

print("请输入数列，数字之间用空格隔开：")
arr=[int(x) for x in input().split()]
merge_sort(arr,0,len(arr)-1)
print(arr)
