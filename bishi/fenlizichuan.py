import sys
str = sys.stdin.readline().strip()


def txt_wrap_by( start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()



newsDate = txt_wrap_by("_*_", "_$_", str)
print newsDate
b = '_*_' + newsDate + '_$_'

print str.find(b)
strs = str.replace(b ,'')
print strs