"""
5928 Contest Timing
"""

D,H,M = map(int, input().split())
start = 11*60 + 11
end = (D-11)*24*60 + H*60 + M
if start > end:
    print(-1)
else:
    print(end-start)
#print((D-11)*24*60+(H-11)*60+M-11)
