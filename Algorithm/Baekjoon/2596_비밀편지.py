"""
2596 비밀편지

6자리이므로, 2^6 만큼 미리 돌면서 1 차이 나는 걸 계산하는 방법도 있다
각 알파벳마다 6개만 만들면 되므로, 하드코딩도 가능하다.
미리 만드는 버전: https://www.acmicpc.net/source/2905117
하드코딩 버전: https://www.acmicpc.net/source/45918141

내 풀이는 둘의 차이(XOR 결과)가 2 이하로 난다면,
2의 배수이기 때문에
2의 배수 & (2의 배수-1) 은 0 이 된다는 성질을 이용하였다.
(미리 해두는 preprocessing 과정 없음)

그리고 1개 차이 나는 게 여러 개 있을 수 있다고 생각해서 예외 처리를 두었는데,
(flag 이용) 다른 코드들을 보니 그런 예외는 없는 것으로 보인다.
"""

# 주어진 문자들로는 1개 차이가 여러 개 날 수 없음
# 필요없는 로직 제거 & break 를 더 빨리 함
# 속도 개선 효과 없었음
N = int(input())
letter = input()
length = len(letter)
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
num = [0b000000, 0b001111, 0b010011, 0b011100, 0b100110, 0b101001, 0b110101, 0b111010]
ans = []

for i in range(length//6):
    cur = 0
    for j in range(6):
        cur <<= 1
        cur |= int(letter[i*6+j])

    flag = 0
    ret = 0
    for j in range(8):
        if num[j] == cur:
            flag = 1
            ret = j
            break
        else:
            diff = num[j] ^ cur
            if (diff & (diff-1)) == 0:
                flag = 1
                ret = j
                break
    if flag:
        ans.append(alpha[ret])
    else:
        print(i+1)
        break
else:
    print(*ans, sep="")

# 2022.07.13 최초 통과 버전
"""
N = int(input())
letter = input()
length = len(letter)
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
num = [0b000000, 0b001111, 0b010011, 0b011100, 0b100110, 0b101001, 0b110101, 0b111010]
ans = []

for i in range(length//6):
    cur = 0
    for j in range(6):
        cur <<= 1
        cur |= int(letter[i*6+j])

    flag = 0
    ret = 0
    for j in range(8):
        if num[j] == cur:
            flag = 1
            ret = j
            break
        else:
            diff = num[j] ^ cur
            if (diff & (diff-1)) == 0:
                if flag:
                    flag = 0
                    break
                flag = 1
                ret = j
    if flag:
        ans.append(alpha[ret])
    else:
        print(i+1)
        break
else:
    print(*ans, sep="")
"""
