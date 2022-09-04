/*
10926 ??!

입력, 출력 기초 연습
Go 언어 입력받는 방법 Scanf
https://sungmin-joo.tistory.com/10
Go 언어 주석 사용법 (C와 동일)
https://thebook.io/006806/ch02/01/05/
*/
package main

import "fmt"

func main() {
    var id string
    fmt.Scanf("%s", &id)
    fmt.Printf("%s??!\n", id)
}