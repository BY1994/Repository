"""
10448 유레카 이론
"""

tri = []
eureka = [0]*1001
tri_len = 0
for i in range(1,50):
    tri.append(i*(i+1)//2)
    tri_len += 1

for i in range(tri_len):
    for j in range(tri_len):
        for k in range(tri_len):
            num = tri[i]+tri[j]+tri[k]
            if num > 1000: continue
            eureka[num] = 1
    
for _ in range(int(input())):
    print(1 if eureka[int(input())] == 1 else 0)


# 삼각수 중복 가능한데 중복 고려 안함
"""
tri = []
eureka = [0]*1001
tri_len = 0
for i in range(1,50):
    tri.append(i*(i+1)//2)
    tri_len += 1

for i in range(tri_len):
    for j in range(i+1, tri_len):
        for k in range(j+1, tri_len):
            num = tri[i]+tri[j]+tri[k]
            if num > 1000: continue
            eureka[num] = 1
    
for _ in range(int(input())):
    print(1 if eureka[int(input())] == 1 else 0)
""" 


"""
https://www.acmicpc.net/board/view/25649

사실 범위 [3,1000] 내에서 답이 0인 경우는 4 6 11 20 29 다섯 가지밖에 없습니다.

나머지 경우에 모두 1이 나오는지 테스트해보세요.

1000 이하인 삼각수가 몇 개나 될 지 생각해보시고, 더 간단하고 짧은 브루트 포스 솔루션을 작성해보시면 좋을 것 같습니다.
"""
