# 1
"""
for tc in range(int(input())):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    print("Case #{}: {}".format(tc+1, sum(C) % M))
"""

# 2
"""
vowel = ['A','E','I','O','U','a','e','i','o','u']
y = ['Y', 'y']
for tc in range(int(input())):
    name = input()
    if name[-1] in vowel:
        print("Case #{}: {} is ruled by Alice.".format(tc+1, name))
    elif name[-1] in y:
        print("Case #{}: {} is ruled by nobody.".format(tc+1, name))
    else:
        print("Case #{}: {} is ruled by Bob.".format(tc+1, name))
"""
# 3
# 3-1. Time Limit
"""
for tc in range(int(input())):
    N = int(input())
    C = list(map(int, input().split()))

    ans = []
    for i in range(N): # i까지만 돌도록...
        for j in range(i, -1, -1): # citation 크기 정하고
            cur = 0
            for k in range(i+1): # 여기까지 돌면서 체크
                if C[k] >= j+1:
                    cur += 1
            if cur >= j+1:
                ans.append(j+1)
                break
    print("Case #"+str(tc+1)+": "+' '.join(map(str, ans)))
"""
# 3-2. Success
"""
import sys
input = sys.stdin.readline

def search(i, start, end, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return segment_tree[i]
    mid = start + (end - start) // 2
    return search(i * 2, start, mid, left, right) + \
               search(i * 2 + 1, mid + 1, end, left, right)

def update(i, start, end, idx, value):
    if end < idx or idx < start:
        return 0
    if start == end == idx:
        segment_tree[i] += value
        return segment_tree[i]
    mid = start + (end - start) // 2
    update(i*2, start, mid, idx, value)
    update(i*2+1, mid+1, end, idx, value)
    segment_tree[i] = segment_tree[i*2] + \
               segment_tree[i*2+1]
    return segment_tree[i]


segment_tree =[0]*4*(10**5)

for tc in range(int(input())):
    print("Case #"+str(tc+1)+": ", end="")
    N = int(input())
    C = list(map(int, input().split()))

    # init    
    for i in range(4*(10**5)):
        segment_tree[i] = 0

    # update & query
    cur = 0
    for i in range(N):
        update(1, 0, 10**5, C[i], 1)
        if sea
        rch(1, 0, 10**5, cur+1, 10**5) >= cur+1:
            cur += 1
        print(cur, end=" ")
    print()
"""

# 3 Answer
import heapq

def calculate_hindex(N: int, citations: list):
    minH = []
    ans = []
    hindex = 0
    for i in range(N):
        if citations[i] > hindex:
            heapq.heappush(minH, citations[i])
        while minH and minH[0] <= hindex:
            heap.heappop(minH)
        if len(minH) >= hindex+1:
            hindex += 1
        ans.append(hindex)
    return ans

# 4
"""
BBBB
.BB.
RRR.
RRRR

Impossible 이 답
파란색 돌을 뒀을 때 게임이 끝나기 때문에,
빨간색 돌이 하나 더 많을 수 없음

Test Set 1을 돌려보니
2
.R
BB
정답은 Blue wins 인데 Nobody wins 가 나옴
if y == n-1 or x == n-1: 이 조건 때문에 탐색이 안 끝났는데
마지막 줄이라는 이유로 끝나버림 (마지막 줄인데 오른쪽으로 탐색해야하는 경우)

Test Set 1 에 반례
9
BRRRBRBBR
BBRRRBRRB
BRRRRBBRR
BBRBBBBBB
RBRRBBRRR
RRBRR.RBB
BBBBRRRBR
RBBRBRBRR
BBBRBRBBR

정답은 Red winds 인데 나는 Impossible 출력
두 갈래로 내려가는 길이 생겨서 R 성공 경로가 2개라고 잡혔는데,
마지막에 중간 지점에 빨간 돌을 두는 것이 가능할 듯
"""
# Wrong Answer

visited = [[0 for i in range(101)] for j in range(101)]

def dfs(BR, x, y, n):
    global Rwin, Bwin, board, visited#, flag

    #print(BR, x, y, n)
    if y == n-1 and BR == 0:
        #flag = 1
        Bwin += 1
        return
    if x == n-1 and BR == 1:
        #flag = 1
        print(BR, x, y, n)
        Rwin += 1
        return
    #if y == n-1 or x == n-1:
    #    return
    
    # next
    for nextx, nexty in (x+1, y), (x+1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1):
        if nextx < 0 or nextx >= n or nexty < 0 or nexty >= n:
            continue
        if visited[nextx][nexty] == 1:
            continue
        if BR == 0 and board[nextx][nexty] == 'B':
            visited[nextx][nexty] = 1
            dfs(BR, nextx, nexty, n)
            #visited[nextx][nexty] = 0
        elif BR == 1 and board[nextx][nexty] == 'R':
            visited[nextx][nexty] = 1
            dfs(BR, nextx, nexty, n)
            #visited[nextx][nexty] = 0

for tc in range(int(input())):
    n = int(input())

    totalB = 0
    totalR = 0

    board = []
    for _ in range(n):
        board.append(input())
        totalB += board[_].count('B')
        totalR += board[_].count('R')
    if abs(totalB - totalR) > 1:
        print("Case #"+str(tc+1)+": "+'Impossible')
    else:
        #visited = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                visited[i][j] = 0

        Bwin = 0
        Rwin = 0

        # row -> B
        for i in range(n):
            if board[i][0] == 'B':
                #flag = 0
                visited[i][0] = 1
                dfs(0, i, 0, n)
                #visited[i][0] = 0
                #if flag == 1:
                    #Bwin += 1
                    #break
        #count
        #cnt1 = 0
        #cnt2 = 0
        #for i in range(n):
        #    if visited[i][n-1] == 0:
        #        if board[i][n-1] == 'B':
        #            Bwin += 1
        
            #if board[i][0] == 'B':
            #    cnt1 += 1
            #if board[i][n-1] == 'B':
            #    cnt2 +=1
        #if Bwin > 0:
            #if cnt1 > 1 and cnt2 > 1:
                #Bwin +=1

        # col -> R
        for j in range(n):
            if board[0][j] == 'R':
                #flag = 0
                visited[0][j] = 1
                dfs(1, 0, j, n)
                #visited[0][j] = 0
                #if flag == 1:
                #    Rwin += 1
                #    break

        #cnt1 =0
        #cnt2 = 0
        #for j in range(n):
        #    if board[0][j] == 'R':
        #        cnt1 += 1
        #    if board[n-1][j] == 'R':
        #        cnt2 += 1
        #if Rwin > 0:
        #    if cnt1 > 1 and cnt2 > 1:
        #        Rwin += 1

        if Bwin + Rwin > 1:
            print("Case #"+str(tc+1)+": "+'Impossible')
        elif Bwin == 1:
            if totalB < totalR:
                print("Case #"+str(tc+1)+": "+'Impossible')
            else:
                print("Case #"+str(tc+1)+": "+'Blue wins')
        elif Rwin == 1:
            if totalR < totalB:
                print("Case #"+str(tc+1)+": "+'Impossible')
            else:
                print("Case #"+str(tc+1)+": "+'Red wins')
        else:
            print("Case #"+str(tc+1)+": "+'Nobody wins')

# 4. Answer - Flood fill approach
def check_winner(board, n):
    for i in range(n):
        if board[i][0] == 'B':
            flood(board, i, 0, n, 'B')
        if board[0][i] == 'R':
            flood(board, 0, i, n, 'R')

    for i in range(n):
        if board[i][n-1] == 'b':
            return 'B'
        if board[n-1][i] == 'r':
            return 'R'

    return '.'

DIRECTIONS = ((0,1), (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0))

def flood(board, row, col, n, colour):
    board[row][col] = colour.lower()
    for direction in DIRECTIONS:
        new_row, new_col = row + direction[0], col + direction[1]
        if 0 <= new_row < n and 0 <= new_col < n:
            if board[new_row][new_col] == colour:
                flood(board, new_row, new_col, n, colour)
    
def solve(original_board, n):

    num_red, num_blu = count_stones(original_board)
    if abs(num_red - num_blu) > 1: # Red and Blue have not taken turns properly.
        return 'Impossible'

    board = deepcopy(original_board)
    winner = check_winner(board, n)
    if winner == '.':
        return 'Nobody wins'

    if (winner == 'B' and num_blu < num_red) or (winner == 'R' and num_red < num_blu):
        return 'Impossible'

    for row in range(n):
        for col in range(n):
            if original_board[row][col] == winner:
                board = deepcopy(original_board)
                board[row][col] = '.'
                if check_winner(board, n) == '.':
                    if winner == 'B':
                        return 'Blue wins'
                    elif winner == 'R':
                        return 'Red wins'

    return 'Impossible'

# 4. Answer - Path tracing approach
def blue_path_south(padded_board, m):
    # Start at the southwest corner with a blue stone on the left and a red stone on the right.
    left, right = (m-1, 0), (m-1, 1)
    path = set()
    # Follow a path between the hexes, always keeping blue stones on the left.
    while left[1] < m - 1: # Stop when we reach the east side.
        path.add(left)
        left, right = step(padded_board, 'B', left, right)
        if right[0] == 0: # Break if we reach the north side.
            return None
        return path

def step(padded_board, colour, left, right):
    next_hex = get_next_hex(left, right)
    if padded_board[next_hex[0]][next_hex[1]] == colour:
        return next_hex, right
    else:
        return left, next_hex

def get_next_hex(left, right):
    # Find where the "right hex" is, relative to the "left hex",
    # then, return the "next hex" (in counterclockwise order).
    #    / ＼/ ＼
    #   ｜2 ｜1 ｜
    #   / ＼/ ＼/ ＼
    #  ｜3 ｜* ｜0 ｜
    #   ＼ /＼ /＼ /
    #    ｜4 ｜5 ｜
    #     ＼ /＼ /
    # The "left hex" is the middle hex in the diagram above,
    # where the numbers on the outer hexes correspond to the index of
    # that hex in the DIRECTIONS tuple.
    right_dir = (right[0] - left[0], right[1] - left[1])
    for index, direction in enumerate(DIRECTIONS):
        if right_dir == direction:
            next_dir = DIRECTIONS[(index + 1) % 6]
            return (left[0] + next_dir[0], left[1] + next_dir[1])

    raise Exception

def solve(board, n):
    num_red, num_blu = count_stones(board)
    if abs(num_red - num_blu) > 1: # Red and Blue have not taken turns properly.
        return 'Impossible'

    # Pad the board to treat the edges of the board as coloured stones, and also
    # so we always have the same valid start positions for the paths.
    padded_board = pad_board(board, n)
    m = n+2

    south_path = blue_path_south(padded_board, m)
    if south_path:
        north_path = blue_path_north(paaded_board, m)
        common_blue_stones = south_path.intersection(north_path)
        if common_blue_stones and num_blu >= num_red:
            return 'Blue wins'
        else:
            return 'Impossible' # Blue already won before the last stone was placed.

    west_path = red_path_west(padded_board, m)
    if west_path:
        east_path = red_path_east(padded_board, m)
        common_red_stones = west_path.intersection(east_path)
        if common_red_stones and num_red >= num_blu:
            return 'Red wins'
        else:
            return 'Impossible' # Red already won before the last stone was placed.

        return 'Nobody wins'
    
# 5
"""
import sys
input = sys.stdin.readline

def check(visited):
    global M, P
    for i in range(M):
        if forb[i] == visited:
            return 0
        #for j in range(P):
        #    if forb[i][j] != visited[j]:
        #        break
        #else: # same
        #    return 0
    return 1

def dfs(depth, total, number):
    global P, _min
    if total >= _min:
        return
    if depth == P-1:
        if check(number):
            _min = min(_min, total)
        return

    #visited[depth+1] = '1'
    dfs(depth+1, total + cnt0[depth+1], number * 10 + 1)
    #visited[depth+1] = '0'
    dfs(depth+1, total + cnt1[depth+1], number*10)

for tc in range(int(input())):
    N, M, P = map(int, input().split())
    friend = []
    forb = []
    for i in range(N):
        friend.append(input())
    for i in range(M):
        forb.append(int(input()))
        #forb.append(input())

    cnt1 = [0] * P
    cnt0 = [0] * P
    for i in range(P):
        for j in range(N):
            if friend[j][i] == '1':
                cnt1[i] += 1
            else:
                cnt0[i] += 1

    # dfs
    _min = 10000
    #visited = 0
    #visited = [0] * P
    #visited[0] = '1'
    dfs(0, cnt0[0], 1) # opposite
    #visited[0] = '0'
    dfs(0, cnt1[0], 0)

    print("Case #{}: {}".format(tc+1, _min))
"""

# Answer
# Representing the Tea
static class scoredTea implements Comparable<ScoredTea> {
    final int score;
    final String tea;

    ScoredTea(int score, String tea) {
        this.score = score;
        this.tea = tea;
    }

    @Override
    public int compareTo(ScoredTea o) {
        return score - o.score;
    }
}

# Scoring the tea
private static int compare(String prefix, String tea) {
    int difference = 0;
    for (int i = 0; i < prefix.length(); i++) {
        if (prefix.charAt(i) != tea.charAt(i)) {
            difference++;
        }
    }
    return difference;
}

private static int score(String prefix, String [] teas) {
    int difference = 0;
    for (String tea: teas) {
        difference += compare(prefix, tea);
    }
    return difference;
}

# 1. S = {""}
# 2. For each binary string bi in Sn-1 add bi + "0" and bi + "1" to Sn
# 3. Filter out the best M +1 teas in Sn
# 4. Repeat 2-3 until Sp

List<ScoredTea> q = new ArrayList<>();
q.add(new ScoredTea(0, ""));

for (int i = 0; i < length; i++){
    List<ScoredTea> next = new ArrayList(q.size() *2);

    for (ScoredTea s: q) {
        expand(next, s.tea, teas);
    }

    Collections.sort(next);

    q.clear();
    for (int j = 0; j < size && j < next.size(); j++) {
        q.add(next.get(j));
    }
}

public static void expand(List<ScoredTea> list, String prefix, String[] teas){
    String zero = prefix + "0";
    list.add(new ScoredTea(score(zero, teas), zero));

    String one = prefix + "1";
    list.add(new ScoredTea(score(one, teas), one));
}

for (ScoredTea s: q){
    if (!forbiddens.contains(s.tea)) {
        return s.tea;
    }
}

# Optimization
# Preconstruction: count the number of 0 and 1 for each bit position

private static int scores[][];
private static void buildScores(String[] teas) {
    scores = new int[teas[0].length()][2];
    for (int i = 0; i < teas[0].length(); i++) {
        scores[i][0] = scores[i][1] = 0;
        for (int j = 0; j < teas.length; j++) {
            if (teas[j].charAt(i) == '0') {
                scores[i][1]++;
            } else {
                scores[i][0]++;
            }
        }
    }
}

public static void expand(List<ScoredTea> list, String prefix, String[] teas){
    String zero = prefix + "0";
    list.add(new ScoredTea(prefix.score + scores[prefix.tea.legnth()][0], zero));

    String one = prefix + "1";
    list.add(new ScoredTea(prefix.score + scores[prefix.tea.legnth()][1], one));
}
