/*
25191 치킨댄스를 추는 곰곰이를 본 임스

import "math" 하고
math.Min(A,B) 로 사용하려고 했는데,
go 언어의 Min 은 float64 타입만 지원하기 때문에
int 는 인자로 넣을 수 없다고 한다.
stack overflow 에서 직접 선언해서 사용하라고 해서 해당 방법을 사용하였다.
https://stackoverflow.com/questions/27516387/what-is-the-correct-way-to-find-the-min-between-two-integers-in-go
https://learnandlearn.com/golang-programming/golang-reference/golang-find-the-minimum-value-min-function-examples-explanation
*/
package main

import "fmt"
//import "math"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
    var N, A, B int
    fmt.Scanf("%d", &N)
    fmt.Scanf("%d %d", &A, &B)
    fmt.Printf("%d\n", min(N, A/2 + B))
    //fmt.Printf("%d\n", math.Min(N, A/2 + B))
}