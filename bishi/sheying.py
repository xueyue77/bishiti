import sys


# if weizhi < amin:
#     print amin - weizhi
# if weizhi > amax:
#     print amax - weizhi
# if weizhi >= amin and weizhi <= amax:
#     print 0

while 1:

    line1 = map(int, sys.stdin.readline().strip().split())
    #s = raw_input()
    # raw_input()里面不要有任何提示信息
    if line1 != "":
        #line1 = map(int, sys.stdin.readline().strip().split())
        a = line1[0]
        weizhi = line1[1]

        b = [[0 for i in range(2)] for i in range(a)]
        for i in range(a):
            line = map(int, sys.stdin.readline().strip().split())
            b[i] = line
        # print b
        minlist = []
        maxlist = []
        for i in range(a):
            minlist.append(min(b[i]))
            maxlist.append(max(b[i]))
        amin = max(minlist)
        amax = min(maxlist)
        # print amin,amax
        if amin > amax:
            print -1
        elif weizhi < amin:
            print amin - weizhi
        elif weizhi > amax:
            print amax - weizhi
        else:
            print 0
    else:
        break