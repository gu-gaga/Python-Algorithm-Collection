# 双指针（滑动窗口）求最长连续不重复子序列
count={}
n=int(input())
arr=list(map(int,input().split()))
j=0
res=0
for i in range(n):
    count[arr[i]]=count.get(arr[i],0)+1
    while count[arr[i]]>1:
        count[arr[j]] -= 1
        j += 1
    res = max(res, i - j + 1)
print(res)
