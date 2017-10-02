import sys
n1 = int(sys.stdin.readline().strip())
str1 = map(int,sys.stdin.readline().strip().split())
n2 = int(sys.stdin.readline().strip())
str2 = map(int,sys.stdin.readline().strip().split())

for i in str2:
    str1.append(i)


str1.sort()
half = len(str1) / 2
print ((str1[half] + str1[~half]) / 2.0)