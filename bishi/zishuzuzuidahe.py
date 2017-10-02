import sys
def mostLarge(alist):
    tem = 0
    ans = alist[0]
    for i in alist:
        tem = max(tem+i,i)
        ans = max(tem,ans)
    return ans

n = sys.stdin.readline().strip()
line = map(int,sys.stdin.readline().strip().split())
print mostLarge(line)
