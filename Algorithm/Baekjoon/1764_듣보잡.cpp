/*
1764 �躸��

STL ���� (������ ������ �ʿ��ؼ� hash �� ��� ����) 

vector ����
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=4roring&logNo=221337048963

map ����
https://life-with-coding.tistory.com/305
*/
#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

int N, M;
int count;
map<string,int> hear, see;
vector<string> answer;

int main(void)
{
    string name;
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
        cin >> name;
        hear.insert(make_pair(name, i));
    }
    for (int i = 0; i < M; ++i) {
        cin >> name;
        see.insert(make_pair(name, i));
    }

    for (auto i = hear.begin(); i != hear.end(); i++) {
        if (see.find(i->first) != see.end()) {
            count++;
            answer.emplace_back(i->first);
        }
    }
    cout << count << "\n";
    for (auto iter = answer.begin(); iter != answer.end(); ++iter)
    {
        cout << *iter << "\n";
    }
    return 0;    
}
