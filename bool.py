#부울(bool) 자료형 참이나 거짓을 나타내는 값
# True, False 두 (상수-변하지 않는 값)리터럴 만 가진다
a = 1
print(a > 1)
# 연산값을 출력만 하지 저장은 않함 (저장을 하려면 변수에 담아야 함)
print(a < 10)

b = a > 1 # 연산결과를 b에 저장함
print(b, type(b)) # type 함수를 사용하여 확인 -> False <class 'bool'>

print(b * 10) # 성립하지 않는 연산
# False 는 정수로 반환하면 0이기 때문에 산술연산하면 0이 나옴

print(True * False) # True 는 정수로 반환하면 1이기 때문에 산술연산하면 0이 나옴