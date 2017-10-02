import sys

# a = list(str)
# for i in a:
#     for j in a:
#         if j == i:
#             a.pop(j)
# print a
from collections import OrderedDict
str = sys.stdin.readline().strip()
print "".join(OrderedDict.fromkeys(str))

aa = []
def  findMinMis(A):
    for i in A:
        if i > 0:
            aa.append(i)

    N = max(len(A),max(A))
    alist = (N+1) * [0]
    alist[0] = 1
    A = list(set(A))
    for i in A:
        alist[i] += 1

    for j in range(N+1):
        if alist[j] == 0:
            return j

def  findMinMis(A):
    l = 0
    a = len(A)

    while(l < a):
        if A[l] == l+1:
            l += 1
        elif A[l]<= l or A[l] > a or A[A[l]-1] == A[l]:
            A[l] = A[l-1]
            l -= 1
        else:
            temp = A[l]
            A[l] = A[A[l]-1]
            A[temp - 1] = temp
    return l+1