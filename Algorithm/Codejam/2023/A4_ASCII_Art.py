"""
Codejam2023 A round
ASCII Art

for 문을 직접 순회하면 시간초과가 날 것이라고 생각했는데, 통과함
ABCDE...ZAABBCCDD...ZZAAABBB 이렇게 증가하므로 규칙을 한 번에 찾을 수 있을 것이라고 생각했는데
바로 찾기는 어려웠다.
"""

import math

for tc in range(int(input())):
    N = int(input())
    rem = 0
    for i in range(1, 10**6):
        if i * (i+1) * 13 >= N:
            rem = i
            N -= (i-1)*i*13
            break
    result = chr(math.ceil(N/rem) + 65 -1)
    print(f"Case #{tc+1}: {result}")
