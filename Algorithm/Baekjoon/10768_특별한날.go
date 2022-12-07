/*
10768 특별한 날

if 문을 줄이려고 *100 으로 계산하였다.
2줄 연속으로 입력을 받을 때 \n 처리가 어떻게 되는지 궁금하다.
아래와 같이 풀이하였는데 문제는 발생하지 않았다.
*/
package main

import "fmt"

func main() {
    var M, D int
    fmt.Scanf("%d", &M)
    fmt.Scanf("%d", &D)
    D += M*100
    if D == 218 {
        fmt.Printf("Special\n")
    } else if D < 218 {
        fmt.Printf("Before\n")
    } else {
        fmt.Printf("After\n")
    }
}