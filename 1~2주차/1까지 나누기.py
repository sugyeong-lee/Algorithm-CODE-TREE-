n = int(input())
k=0
for i in range(1, n+1):
    if n>1:
        n //= i
        k+=1
    else:
        print(k)
        break
// 나눗셈 몫을 조심하자! /와 %만 생각했는데 //이 중요하다! 한끗차이이다.
