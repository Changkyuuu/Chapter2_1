# 관계연산자

# a = 2
# a = 3

# 위의경우 2가 3으로 바뀌는게 아니라 저장공간 2 저장공간 3 이 둘다 생성후 a가 3을 가르키게 되는것

# b = a + 10
# 하면 b는 13이 되고 붕 떠버린 2의 저장공간은 python이 알아서 삭제

# 객체의 대소 비교

print(1 > 3) # 1의 저장공간과 3의 저장공간을 비교하고 사라짐
# 변수는 저장공간을 기억해서 계속 사용하는것
print(2 < 4) # 해당은 true 아니면 false 값만

print(1>=3)
print(2<=4)

print( 1 == 3)
print( 2 != 4)

#복합관계식 지원
a = 6
print( 0 < a and a < 10) # 이거 말고 밑에꺼 쓰자 워닝뜸
print(0 < a < 10)

# 수치형 이외 다른 타입 객체 비교
print('abcd' > 'abc')
print('abcd' > 'abcde')
print([1,2,3] > [1,2,2])
print([1,2,3] > [1,2,4])

# 동질성 비교 : ==
# 동일성 비교 : is

a = 20 # a가 20이라는 저장공간을 가르킴
b = 30
c = a # c가 a가 가르키는 20의 저장공간을 같이 바라봄 새로운 20 저장공간을 가르키지 않음

print( a == b) # 동질성 아니므로 거짓
print(a is b) # 동일성 아니므로 거짓
print( a == c) # 동질성 이므로 참
print( a is c) # 동일성 이므로 참


# 논리식의 계산순서

print(True or 'logical') # True 가 출력
print(False or 'logical') # logical 출력

#1 or 0 = 1 앞이 참이면 1
#1 or 1 = 1
#0 or 1 = 1 앞이 0 이면 두
#0 or 0 = 1

#0 and 1 = 0 앤드 앞이 0이면 안해보고 0
#0 and 1 = 0
#1 and 1 = 1 앤드 앞이 1이면 뒤까지 해보고 뒤값
#1 and 0 = 0

print([] or 'logical')
print([10,20] or 'logical')
print('operator' or 'logical')
print('' or 'logical') # 비어있으면 false

print(None or 'logical')
print(None or [])

s = 'Hello Eorld'
s and print(s)
s = ''
s and print(s)

