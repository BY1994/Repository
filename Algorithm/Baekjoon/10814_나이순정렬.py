"""
10814 나이순 정렬
"""

import sys
input = sys.stdin.readline

N = int(input())
check = [0] * 201
member = []
ans = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    member.append([age, name])
    ans.append([age, name])
    check[age] += 1

for i in range(200):
    check[i+1] += check[i]

for i in range(N):
    ind = check[member[i][0]-1]
    ans[ind][0] = member[i][0]
    ans[ind][1] = member[i][1]
    check[member[i][0]-1] += 1

for i in range(N):
    print(*ans[i])

# https://www.acmicpc.net/source/38137537
# Python 와 C++ 풀이 비슷 배열 인덱스 밑에 추가
"""
#include<iostream>
#include<queue>
using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);

	queue<string> q[201];

	int N; cin >> N;
	while (N--)
	{
		int input;
		cin >> input;

		string name;
		cin >> name;
		q[input].push(name);
	}


	for (int i = 1; i <= 200; i++)
	{
		while (!q[i].empty()) {
			cout << i << " " << q[i].front() << '\n';
			q[i].pop();
		}
	}

	return 0;
}
"""
