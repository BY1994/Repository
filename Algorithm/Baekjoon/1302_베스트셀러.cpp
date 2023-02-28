/*
1302 ����Ʈ���� 

���ڿ�
�ؽø� ����� ���հ� �� 

c++ string �� ������ �񱳴� �׳� > �� ����ϸ� �Ǵ� �ſ���.
������ �����ε�
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=iluiou&logNo=220139528466

ó�� �ڵ� ������ �ܶ� ���� ����
1. find() �Լ� ����� index ��� �����߱� ������ 
cannot convert unordered_map find
"If your compiler support C++14 or later, simply return by auto"
https://stackoverflow.com/questions/72699275/conversion-error-in-iterator-over-vector-of-unordered-map
2. index Ÿ���� int �� �ƴѵ� ���� �迭�� index ó�� �����ؼ� 
unordered map no match operator []
https://stackoverflow.com/questions/15660838/error-no-match-for-operator-in-near-match

Ǯ�̸� �ٽ� �����غ���,
compare �Լ� © �� ������ vector �� �ű�� sort �ϴ� ���� ��� Ǯ���� �� ����.
*/

// ���� ����
#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main(void) {
	unordered_map <string, int> ht;
	int N;
	string name;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		cin >> name;
		auto index = ht.find(name);
		if (index != ht.end()) {
			index->second += 1;
		} else ht.insert({name, 0});
	}
	int max = -1;
	string max_name;
	for (auto book: ht) {
		if (book.second > max) {
			max = book.second;
			max_name = book.first;
		} else if (book.second == max && max_name > book.first) {
		    max_name = book.first;
		}
	}
	cout << max_name << endl;
} 

// ���� �ܶ� ���� �ʾ� ���� 
#if 0
#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main(void) {
	unordered_map <string, int> ht;
	int N;
	string name;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		cin >> name;
		int index = ht.find(name);
		if (index != ht.end()) {
			ht[index] += 1;
		} else ht[index] = 0;
	}
	int max = 0;
	for (auto book: ht) {
		if (book.second > max) {
			max = book.second;
		}
	}
	cout << max << endl;
}
#endif
