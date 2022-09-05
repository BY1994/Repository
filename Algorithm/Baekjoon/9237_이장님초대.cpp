/*
9237 이장님 초대

greedy 알고리즘

stl sort 사용방법 
https://m.blog.naver.com/ndb796/221227975229 
*/
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std; 

bool compare(int a, int b) {
	return a > b;
}

int main(void)
{
	int N, tree;
	int max = 1;
	int day = 1;
	vector<int> trees;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &tree);
		trees.push_back(tree);
	}
	sort(trees.begin(), trees.end(), compare);
	for (int i = 0; i < N; i++) {
		if (max < trees[i] + day) max = trees[i] + day;
		day++;
	}
	printf("%d\n", max+1);
	return 0;
}
