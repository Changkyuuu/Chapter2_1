# 정수형 자료형
a = 23
print(a,type(a))
print(isinstance(a,int)) # isinstanc 함수로 a가 int 타입인가?? 맞으면 true 틀리면 false 확인할수 있음

#2진수(01001010) 10진수 8진수 16진수
b = 0b1101 # 2진수
c = 0o23 # 8진수
d = 0x23 # 16진수

print(b)
print(c)
print(d)

# python 3.x에서는 int, long가 합쳐져서 표현범위가 무한대

e = 2**1024
print(e, type(e))
#print(e.bit_length())

# 변환함수
print(oct(38))
print(hex(38))
print(bin(38))