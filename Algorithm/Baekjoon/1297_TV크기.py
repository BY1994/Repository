"""
1297 TV 크기

2**0.5 = 1.414
H^2X^2 + W^2X^2 = D^2
sqrt(X^2) = sqrt(D^2 / (H^2 + W^2))
"""

D, H, W = map(int, input().split())
X = (D**2/(H**2+W**2))**0.5
print(int(H*X), int(W*X))


# https://www.acmicpc.net/source/15520630
"""
d, h, w = map(int, input().split())
hw = (h**2+w**2)**0.5
print(int(d*h/hw+1e-9),int(d*w/hw+1e-9))
"""
