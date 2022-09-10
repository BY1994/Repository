/*
11656 접미사 배열

string array[]; 를 했더니 컴파일 에러가 났다.
array 라는 이름을 키워드로 쓰면 안 되는 것으로 보인다.

string 과 char 배열 간 전환 방법은 시도하다가 타입 에러가 많이 나서
아래의 답변을 참고해서 풀이하였다. 
https://berkbach.com/%EB%B0%B1%EC%A4%80-c-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%92%80%EC%9D%B4-11656%EB%B2%88-73f6748b2840
*/
#include <iostream>
#include <algorithm>

using namespace std;

string input;
string array[1001];
int len;

int main(void)
{
	//scanf("%s", input);
	// len = strlen(input);
	cin >> input;
	len = input.length();
	for (int i = 0; i < len; i++) {
		array[i] = input.substr(i, len);
	}
	/*
	for (int i = 0; i < len; i++) {
		for (int j = i; j < len; j++) {
			array[i].push_back(&input[j]);
			// array[i][j] = input[j];
		}
	}
	sort(array.begin(), array.end());
	*/
	sort(array, array+len);
	for (int i = 0; i < len; i++) {
		//printf("%s\n", array[i]);
		cout << array[i] << "\n";
	}
	return 0;
}
