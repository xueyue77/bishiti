import sys
line = list(sys.stdin.readline().strip())
print line
a = len(line)
for i in range(a):
    line.insert(i,'.')
    for i in range(i+1,a):
        line.insert(i, '.')
        for i in range(i+2,a):
            line.insert(i, '.')
            
print line