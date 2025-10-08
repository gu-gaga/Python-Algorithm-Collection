# 用归并排序求逆序对数量
def merge_sort(arr,l,r):
    if l>=r:
        return 0
    mid=(l+r)//2
    num=merge_sort(arr,l,mid)+merge_sort(arr,mid+1,r)
    tmp=[]
    i,j=l,mid+1
    while i<=mid and j<=r:
        if arr[i]<=arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            num+=mid-i+1
            j+=1
    while i<=mid:
        tmp.append(arr[i])
        i+=1
    while j<=r:
        tmp.append(arr[j])
        j+=1
    for a in range(len(tmp)):
        arr[l+a]=tmp[a]
    return num

print("请输入数列，数字之间用空格隔开：")
arr=[int(x) for x in input().split()]
print(merge_sort(arr,0,len(arr)-1))
