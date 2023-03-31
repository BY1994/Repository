"""
1041 주사위

수학, 그리디

직접 경우의 수를 다 적어보고 그대로 코드로 옮김
    +---+        
    | D |        
+---+---+---+---+
| E | A | B | F |
+---+---+---+---+
    | C |        
    +---+        
이와 같이 서로 마주볼 수 없는 A-F, B-E, C-D 를 제외하고는 모두 2개씩과 3개씩 묶일 수 있다.
2면이 보이는 경우: 6C2 - 맞은편 관계인 3쌍 = 15 - 3 = 12
3면이 보이는 경우: 붙어있는 3개 면을 직접 따져보니 8가지 경우의 수가 나옴
1면이 보이는 경우: 모든 면 중 min 값

3면이 보이는 경우는 맨 위의 모서리 4개만 존재한다.
1면이 보이는 경우는 맨 위에는 아래처럼 (N-2)*(N-2)만 존재한다.
□□□□
□■■□
□■■□
□□□□
그러나 옆면의 경우에는 바닥에 닿는 부분도 1면만 보인다.
□□□□
□■■□
□■■□
□■■□
따라서 두 경우를 더해주면 된다. (N-2)*(N-2)*1 + (N-2)*(N-1)*4
2면이 보이는 경우는 옆 모서리 4곳에 있는 (N-1) 개가 있고,
□□□□
■□□■
■□□■
■□□■
맨 위에 N-2 만큼 4개가 있다
□■■□
■□□■
■□□■
□■■□
따라서 두 경우를 더하면 (N-1)*4 + (N-2)*4 개가 된다.
위의 식들은 N 이 반드시 2 이상이어야하는데,
N 이 1인 경우는 어차피 주사위가 1개 뿐이기 때문에
위의 식이 적용되지 않고 한 주사위의 5면이 모두 사용된다.
따라서 가장 숫자가 큰 한 면만 제외하고 나머지 면이 보이도록 하면 된다.
"""

N = int(input())
dice = list(map(int, input().split()))
if N == 1:
    print(sum(dice)-max(dice))
else:
    plane3 = 4
    plane1 = (N-2)*(N-1)*4 + (N-2)*(N-2)*1
    plane2 = (N-1)*4 + (N-2)*4
    min3 = min([dice[0]+dice[1]+dice[2], dice[0]+dice[1]+dice[3],
                dice[0]+dice[2]+dice[4], dice[0]+dice[3]+dice[4],
                dice[1]+dice[2]+dice[5], dice[1]+dice[3]+dice[5],
                dice[2]+dice[4]+dice[5], dice[3]+dice[4]+dice[5]])
    min2 = min([dice[0]+dice[1], dice[0]+dice[2], dice[0]+dice[3], dice[0]+dice[4],
                dice[1]+dice[2], dice[1]+dice[3], dice[1]+dice[5], dice[2]+dice[4],
                dice[2]+dice[5], dice[3]+dice[4], dice[3]+dice[5], dice[4]+dice[5]])
    min1 = min(dice)
    print(plane1*min1 + plane2*min2 + plane3*min3)
