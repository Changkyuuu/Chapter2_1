# 사칙연산
print(2 * 3)
print(2 + 3)
print(2 - 3)
print(2 / 3)
print(2 / 3.0)
print(2.0 / 3.0)

# //몫 연산자 **(지수승) % 나머지 연산
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# divmod() 함수
print(divmod(2,3))

t = divmod(2,3)
print(t, type(t))

a, b = divmod(2, 3)
print(a, b)

# 연산자 우선순위
print(2 + 3 * 4)
print(-2 + 3 * 4)
print(-(2 + 3) * 4)

# 결합순서
print(2 ** 3 ** 4)  # 진행방향 <- 3의4승 후 2의 3의4승을 함 즉 2의 81승 값
print((2 ** 3) ** 4)
print(2 ** (3 ** 4)) # print(2 ** 3 ** 4) 와일치
