import sys
line = map(int, sys.stdin.readline().strip().split())
l = len(line)
a = []
first = line[0]
if first < 100:
    a.append(first)
for i in range(1,l):
    if line[i] < 100 and line[i] <= first:
        a.append(line[i])
        first = line[i]

b = map(str,a)
print ' '.join(b)

