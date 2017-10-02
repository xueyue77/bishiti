import sys
def maopao(alist):
    a = len(alist)
    for i in range(0, a):
        for j in range(i + 1, a):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist

n = sys.stdin.readline().strip()
line = map(int,sys.stdin.readline().strip().split())
ans = map(str, maopao(line))
print ' '.join(ans)