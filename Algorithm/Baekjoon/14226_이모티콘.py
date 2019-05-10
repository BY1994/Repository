"""
# BOJ 14226 이모티콘

2019-05-09 최초작성
+ 이런 문제 풀 때 자꾸 visited에 추가하는 것을 깜빡한다....
"""

"""
S = int(input())

start = (1, 0, 0) # 현재 이모티콘, 클립보드, 걸린 시간
lenq = 1
q = [start]
flag = 0 # 1이면 탈출
visited = {}

while lenq > 0:
    for l in range(lenq):
        emo, clip, time = q.pop(0)
        if emo == S:
            flag = 1
            mintime = time
            break
        # 화면에 있는 이모티콘을 모두 복사한다
        if emo != clip and not visited.get((emo, emo)):
            visited[(emo, emo)] = 1
            q.append((emo, emo, time+1))
        # 클립보드에 있는 이모티콘을 붙여넣기한다
        if clip > 0:
            visited[(emo+clip, clip)] = 1
            q.append((emo+clip, clip, time+1))
        # 이모티콘 중 하나를 삭제한다.
        if emo > 0 and not visited.get((emo-1, clip)):
            visited[(emo-1, clip)] = 1
            q.append((emo-1, clip, time+1))
        
    if flag == 1:
        break
    lenq = len(q)
    
print(mintime)
"""

S = int(input())

start = (1, 0, 0) # 현재 이모티콘, 클립보드, 걸린 시간
lenq = 1
q = [start]
flag = 0 # 1이면 탈출
visited = {}

while lenq > 0:
    for l in range(lenq):
        emo, clip, time = q.pop(0)
        if emo + 1 > S:
            continue
        if emo == S or emo + clip == S or emo-1 == S:
            flag = 1
            mintime = time+1
            break
        # 화면에 있는 이모티콘을 모두 복사한다
        if emo != clip and not visited.get((emo, emo)):
            visited[(emo, emo)] = 1
            q.append((emo, emo, time+1))
        # 클립보드에 있는 이모티콘을 붙여넣기한다
        if clip > 0:
            visited[(emo+clip, clip)] = 1
            q.append((emo+clip, clip, time+1))
        # 이모티콘 중 하나를 삭제한다.
        if emo > 0 and not visited.get((emo-1, clip)):
            visited[(emo-1, clip)] = 1
            q.append((emo-1, clip, time+1))
        
    if flag == 1:
        break
    lenq = len(q)
    
print(mintime)
