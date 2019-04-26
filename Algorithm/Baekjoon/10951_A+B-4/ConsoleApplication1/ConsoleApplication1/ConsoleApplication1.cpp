// ConsoleApplication1.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include "pch.h"
#include <iostream>

int main() {
	int T;
	signed long long number;
	int sum = 0;
	std::cin >> T;
	std::cin >> number;
	for (int i = 0; i < T; i++) {
		sum += (number % 10);
		number /= 10;
		std::cout << sum << std::endl;
		std::cout << number << std::endl;
	}
	std::cout << sum << std::endl;
	return 0;
}


//11719
/*
#include <iostream>
#include <string>
using namespace std;

int main()
{
	string input;

	for (int i = 0; i < 100; i++)
	{
		getline(cin, input);  // 앤터가 나오기 전 까지 한 줄 입력 
		cout << input << endl;
	}

	return 0;
}
*/


// 11718
/*
#include<iostream>
#include<string>
using namespace std;

int main() {

	string str;
	while (true)
	{
		getline(cin, str);
		if (str == "")
			break;
		cout << str << endl;
	}

	return 0;
}
*/

/* // 스페이스바가 안 나옴!
int main() {
	char A;
	while(std::cin >> A){
		std::cout << A;
	}
	return 0;
}
*/

// 11021
/*
int main() {
	int T, A, B;
	std::cin >> T;
	for (int i = 0; i < T; i++) {
		std::cin >> A >> B;
		std::cout << "Case #" << i + 1 << ": " << A << " + " << B << " = " << A + B << std::endl;
	}
}
*/

// 10953
/*
int main() {
	int T, A, B;
	char comma;
	std::cin >> T;
	for (int i = 0; i < T; i++) {
		//scanf_s("%d,%d", &A, &B);
		std::cin >> A >> comma >> B;
		std::cout << A + B << std::endl;
	}
}
*/

/*
 // 이건 안 돌아간다! 출력 초과 에러가 뜬다!
// 이걸 10952 용으로 수정하기 => 성공!
int main() {
	int a, b;

	while (true) {
		std::cin >> a >> b;
		if (a==0 && b==0){
			break;
		}
		std::cout << a + b << std::endl;
	}
	return 0;
}
*/

/*
int main()
{
	int a, b;

	while (std::cin >> a >> b) {
		std::cout << a + b << std::endl;
	}
	return 0;
}
*/

/*
int main(void){
	int a, b;
	while(scanf("%d %d", &a, &b) != EOF){
		cout << a+b << endl;
	}
	return 0;
}
*/
// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
