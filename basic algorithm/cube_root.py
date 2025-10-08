# 用二分查找求数的三次方根
num=float(input())
l,r=-10000,10000
while r-l>1e-8:
    mid=(l+r)/2
    if mid*mid*mid>=num:
       r=mid
    else:
        l=mid
print(f"{l:.6f}")
