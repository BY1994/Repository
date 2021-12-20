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
