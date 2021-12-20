"""
visited 체크하면 안 되는 문제라고 생각했는데
오른쪽 아래로만 가니까 한번 도달한 지점은 오는 동안 밟은 . 개수가 같다.
"""

def dfs(x, y, depth):
    global H, W, ans
    ans = max(ans, depth)
    for nextx, nexty in ((x+1,y), (x, y+1)):
        if nextx >= H or nexty >= W: continue
        if visited[nextx][nexty] == 1: continue
        if wall[nextx][nexty] == '.':
            visited[nextx][nexty] = 1
            dfs(nextx, nexty, depth+1)

H, W = map(int, input().split())
wall = []
visited = [[0 for _ in range(W)] for __ in range(H)]
ans = 1
for _ in range(H):
    wall.append(input())

dfs(0, 0, 1)
print(ans)


# c로 해도 타임 리밋
"""
#include <stdio.h>

int H;
int W;
char wall[110][110];
int ans;


void dfs(int x, int y, int depth)
{
	//printf("### dfs %d %d %d\n", x, y, depth);
    if (depth > ans) ans = depth;
    int nextx = x+1;
    int nexty = y;
    if ((nextx < H) && (nexty < W)) {
 	   if (wall[nextx][nexty] == '.') {
   	     dfs(nextx, nexty, depth+1);
   	 	}
	}
    
    nextx = x;
    nexty = y+1;
    if ((nextx < H) && (nexty < W)){
	    if (wall[nextx][nexty] == '.') {
	        dfs(nextx, nexty, depth+1);
	    }
	}
}


int main()
{
    scanf("%d %d", &H, &W);
    for (int i = 0; i < H; i++) {
        //for (int j = 0; j < W; j++) {
            scanf("%s", wall[i]);//&wall[i][j]);
        //}
    }
    dfs(0, 0, 1);
    printf("%d\n", ans);

    return 0;
}
"""
