"""
1010 다리 놓기
"""

import math
for tc in range(int(input())):
    N, M = map(int, input().split())
    # mCn
    print(math.factorial(M) // math.factorial(N) // math.factorial(M-N))
