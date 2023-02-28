/*
1302 베스트셀러 

문자열
해시를 사용한 집합과 맵 

c++ string 의 사전식 비교는 그냥 > 를 사용하면 되는 거였다.
연산자 오버로딩
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=iluiou&logNo=220139528466

처음 코드 에러가 잔뜩 났던 이유
1. find() 함수 결과가 index 라고 생각했기 때문에 
cannot convert unordered_map find
"If your compiler support C++14 or later, simply return by auto"
https://stackoverflow.com/questions/72699275/conversion-error-in-iterator-over-vector-of-unordered-map
2. index 타입이 int 가 아닌데 내가 배열의 index 처럼 접근해서 
unordered map no match operator []
https://stackoverflow.com/questions/15660838/error-no-match-for-operator-in-near-match

풀이를 다시 생각해보니,
compare 함수 짤 수 있으니 vector 로 옮기고 sort 하는 것이 모범 풀이일 것 같다.
*/

// 수정 버전
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

// 오류 잔뜩 나는 초안 버전 
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
