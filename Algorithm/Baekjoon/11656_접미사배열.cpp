/*
11656 ���̻� �迭

string array[]; �� �ߴ��� ������ ������ ����.
array ��� �̸��� Ű����� ���� �� �Ǵ� ������ ���δ�.

string �� char �迭 �� ��ȯ ����� �õ��ϴٰ� Ÿ�� ������ ���� ����
�Ʒ��� �亯�� �����ؼ� Ǯ���Ͽ���. 
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
