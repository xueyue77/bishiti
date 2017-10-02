import sys
import re

def checkip(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        print 1
    else:
        print 0

if __name__ == '__main__':

    try:
        while True:
            line = sys.stdin.readline().strip()
            if line == '':
                break
            checkip(line)
    except:
        pass
