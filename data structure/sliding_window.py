# 滑动窗口
from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write
mi=[]
ma=[]
n,k=map(int,input().split())
a=list(map(int,input().split()))
q=deque()
p=deque()
for i in range(n):
    if q and q[0]<=i-k:
        q.popleft()
    while q and a[q[-1]]>=a[i]:
        q.pop()
    q.append(i)
    if i>=k-1:
        mi.append(str(a[q[0]]))
for i in range(n):
    if p and p[0]<=i-k:
        p.popleft()
    while p and a[p[-1]]<=a[i]:
        p.pop()
    p.append(i)
    if i>=k-1:
        ma.append(str(a[p[0]]))
print(" ".join(mi) + "\n" + " ".join(ma) + "\n")
