/*
11943 파일 옮기기
기초 사칙연산 문제
go if, else, func
else 를 if 의 } 뒤에 바로 붙여야하고 줄바꿈 하면 안 됨
math 를 import 하면 math 가 가진 Min 함수는 float 만 받기 때문에 int 용으로 사용할 수 없었음
*/

package main
import "fmt"

func min(x,y int) int {
    if x > y {
        return y
    } else {
        return x
    }
}

func main() {
    var A,B,C,D int
    fmt.Scanln(&A,&B)
    fmt.Scanln(&C,&D)
    fmt.Println(min(B+C,A+D))
}