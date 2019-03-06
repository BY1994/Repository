""" 
백준 알고리즘 1713
후보추천하기

문제)
월드초등학교 학생회장 후보는 일정 기간 동안 전체 학생의 추천에 의하여 정해진 수만큼 선정된다. 그래서 학교 홈페이지에 추천받은 학생의 사진을 게시할 수 있는 사진틀을 후보의 수만큼 만들었다. 추천받은 학생의 사진을 사진틀에 게시하고 추천받은 횟수를 표시하는 규칙은 다음과 같다.
학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 게시된 지 가장 오래된 사진을 삭제한다.
현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.
후보의 수 즉, 사진틀의 개수와 전체 학생의 추천 결과가 추천받은 순서대로 주어졌을 때, 최종 후보가 누구인지 결정하는 프로그램을 작성하시오.

입력)
첫째 줄에는 사진틀의 개수 N이 주어진다. (1≤N≤20) 둘째 줄에는 전체 학생의 총 추천 횟수가 주어지고, 셋째 줄에는 추천받은 학생을 나타내는 번호가 빈 칸을 사이에 두고 추천받은 순서대로 주어진다. 총 추천 횟수는 1,000번 이하이며 학생을 나타내는 번호는 1부터 100까지의 자연수이다.

출력)
사진틀에 사진이 게재된 최종 후보의 학생 번호를 증가하는 순서대로 출력한다.

최초 작성 2019.03.06 PBY
"""

N = int(input()) # 사진틀 크기
recom = int(input()) # 학생들의 추천 횟수
candi = input().split()

pictures = [0] * N
picnum = [0] * N # student를 저장 (몇 번째로 들어왔는지)
picrecom = [0] * N # recommend를 저장

for student in range(recom):
        
        # 내가 있는지 먼저 체크하기
        for p in range(N):
                if pictures[p] == int(candi[student]):
                        picrecom[p] += 1
                        break
                
        else: # 이 단계에서 비어있는 곳 찾는 거랑 min 값 찾기를 동시에 진행
                # 어차피 비어있는 곳이 없으면 min을 이용해야 하니까
                minrecom = recom
                minpicnum = recom
                for p in range(N):
                        if pictures[p] == 0: # 비어있는 곳을 찾으면 넣고
                                pictures[p] = int(candi[student])
                                picnum[p] = student
                                picrecom[p] = 1
                                break
                        
                        # min값 찾기도 동시에 진행
                        if minrecom > picrecom[p]:
                                minrecom = picrecom[p]
                                minpicnum = picnum[p] # 들어온 순서를 비교해야하는데, 이걸 넣지 않았다!!!!
                                minnum = p
                        elif minrecom == picrecom[p] and minpicnum >= picnum[p]: # 같은 추천횟수이면서 더 오래 된 것 저장
                                minrecom = picrecom[p] # 들어온 순서를 넣어야 하는데 여길 p라고 잘못 넣었다!!! 그러면 안 돌아가지!!!
                                minpicnum = picnum[p]
                                minnum = p
                                
                else: # 비어있는 곳을 찾지 못한 경우 그 자리에 내가 들어가야 한다. => 이걸 안하고 건너뛰어서 꽉찬 경우 학생이 아예 들어오지 못함
                        pictures[minnum] = int(candi[student])
                        picnum[minnum] = student
                        picrecom[minnum] = 1                
                        
print(' '.join(map(str,sorted(pictures))))


"""
다음의 부분은 아예 필요가 없었다. for else로 들어들어 온 경우에는 그냥 내가 min 자리를 차지하면 된다.
#                        if student == recom -1:
#                                continue # 마지막 학생이 0이 되지 않게 처리해야함
                        # 추천 적은 & 오래된 학생 빼기
#                        pictures[minnum] = picnum[minnum] = picrecom[minnum] = 0
                        # 0으로 만들 고 그 자리에 내가 들어가야 한다.
"""

# visual studio는 실행시 ctrl + f5
