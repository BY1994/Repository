""" 
8979 올림픽
문제 내용)
올림픽은 참가에 의의가 있기에 공식적으로는 국가간 순위를 정하지 않는다. 그러나, 많은 사람들이 자신의 국가가 얼마나 잘 하는지에 관심이 많기 때문에 비공식적으로는 국가간 순위를 정하고 있다. 두 나라가 각각 얻은 금, 은, 동메달 수가 주어지면, 보통 다음 규칙을 따라 어느 나라가 더 잘했는지 결정한다.
금메달 수가 더 많은 나라 
금메달 수가 같으면, 은메달 수가 더 많은 나라
금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라 
각 국가는 1부터 N 사이의 정수로 표현된다. 한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의된다. 만약 두 나라가 금, 은, 동메달 수가 모두 같다면 두 나라의 등수는 같다. 예를 들어, 1번 국가가 금메달 1개, 은메달 1개를 얻었고, 2번 국가와 3번 국가가 모두 은메달 1개를 얻었으며, 4번 국가는 메달을 얻지 못하였다면, 1번 국가가 1등, 2번 국가와 3번 국가가 공동 2등, 4번 국가가 4등이 된다. 이 경우 3등은 없다. 
각 국가의 금, 은, 동메달 정보를 입력받아서, 어느 국가가 몇 등을 했는지 알려주는 프로그램을 작성하시오. 

입력)
입력의 첫 줄은 국가의 수 N(1 ≤ N ≤ 1,000)과 등수를 알고 싶은 국가 K(1 ≤ K ≤ N)가 빈칸을 사이에 두고 주어진다. 각 국가는 1부터 N 사이의 정수로 표현된다. 이후 N개의 각 줄에는 차례대로 각 국가를 나타내는 정수와 이 국가가 얻은 금, 은, 동메달의 수가 빈칸을 사이에 두고 주어진다. 전체 메달 수의 총합은 1,000,000 이하이다.

출력)
출력은 단 한 줄이며, 입력받은 국가 K의 등수를 하나의 정수로 출력한다. 등수는 반드시 문제에서 정의된 방식을 따라야 한다. 

최초작성 2019.03.03 PBY
최종제출 2019.03.04
"""

countries, rank = list(map(int, input().split()))
ranks = []

for country in range(countries):
    ranks.append(list(map(int, input().split())))

# 내 앞에 몇 명이 있는지 세기 => 전세월세님 방법

# 내 국가가 몇 번째인지 알아야한다.-> 계속 틀린 이유
for country in range(countries):
    if ranks[country][0] == rank:
        saveRank = country
        break

# 그 국가랑 다른 국가 비교
cnt = 0
for country in range(countries):
    if ranks[country][0] == rank:
        continue # 내 국가의 등수는 패스하기
    
    if ranks[country][1] > ranks[saveRank][1]:
       cnt += 1
    elif ranks[country][1] == ranks[saveRank][1]:
        if ranks[country][2] > ranks[saveRank][2]:
            cnt += 1
        elif ranks[country][2] == ranks[saveRank][2]:
            if ranks[country][3] > ranks[saveRank][3]:
                cnt += 1
    # 나보다 작은 경우는 내 뒤 등수이고, 나와 같은 경우는 나랑 같은 등수
    
print(cnt+1)

"""
틀렸습니다 => 입력이 항상 1, 2, 3, 4 국가 순서로 들어오는게 아니라고 한다.
내 국가가 몇 번째에 해당하는지를 체크하는 구문을 따로 둬서
패스하였다!

"""


"""
런타임 에러 => gold가 너무 커서인 것 같다.

# 이거를 해싱함수 같은 느낌으로 수치로 비교하게 만들 수 있을까
# 최대 총합의 수는 1000000인데,
gold = 1000000 * 1000000 * 1000000
silver = 1000000*1000000
copper = 1000000

simple_ranks = []
for country in range(countries):
    simple_ranks.append([ranks[country][0], ranks[country][1]*gold+ranks[country][2]*silver+ranks[country][3]*copper])
sorted_rank = sorted(simple_ranks, key = lambda x: x[1])

cur_rank = 1
same = 0
# 등수를 저장해둬야함 = > 이거 때문에 아까 틀림
for country in range(countries-1, 0, -1):
    if sorted_rank[country][1] > sorted_rank[country-1][1]:
        sorted_rank[country].append(cur_rank)
        cur_rank += same + 1
        same = 0 # 연속으로 몇 번 같은 등수인지
    elif sorted_rank[country][1] == sorted_rank[country-1][1]:
        sorted_rank[country].append(cur_rank)
        same += 1 # 연속으로 둘이 같은 등수
        # 증가 시키지 않음!
    # 정렬시켜서 작은 경우는 없음
    
# 등수를 알고 싶은 국가
for country in range(countries):
    if sorted_rank[country][0] == rank:
        print(sorted_rank[country][2])
        break
"""

"""
# 버블 정렬로 등수 구현 # 동점이 있어서 버블 정렬이면 안 됨 => 정렬 자체가 안 
for i in range(countries):
    for j in range(0, countries-i-1): # 끝까지 정렬되면 하나씩 줄여도 됨, j+1때문에 -1 해줌
        if ranks[j][1] > ranks[j+1][1]:
            rank[j+1], rank[j] = rank[j][:], rank[j+1][:]
        elif rank[j][1] == ranks[j+1][1]:
            if ranks[j][2] > ranks[j+1][2]:
                rank[j+1], rank[j] = rank[j][:], rank[j+1][:]
            elif ranks[j][2] == ranks[j+1][2]:
                if ranks[j][3] > ranks[j+1][3]:
                    rank[j+1], rank[j] = rank[j][:], rank[j+1][:]
                elif ranks[j][3] == ranks[j+1][3]:
                    # 여기가 구현이 안 됨!!!!
"""                    
        
    

# visual studio는 실행시 ctrl + f5

