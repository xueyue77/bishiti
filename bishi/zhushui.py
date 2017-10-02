import sys
line1 = map(int,sys.stdin.readline().strip().split())
line2 = map(int,sys.stdin.readline().strip().split())
a = max(line2)
print '%.2f' % (float(a)/line1[-1])