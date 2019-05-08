# 한줄 문자열

s = ''
str1 = 'Hello World'
str2 = 'Hello World'

print(type(s), type(str1), type(str2))
print(isinstance(str2,str))
print(isinstance(str2,int))

# 여러줄 문자열
str3 = '''''ABCDEFG
DEF
가나다라마바사
아자차카타파하'''''

print(str3)

# 여러줄 주술 -> 여러줄 문자열을 사용한다

'''
주석1
주석2
주석3
'''

#esscape
print('hello\nworld\n')
print('I Say \"HelloWorld\"')
print('I Say "HelloWorld"')
print('She\'s Mom')
print("She's Mom")
print("둘리\t000-0000-0000")

#문자열 연산
str1 = "First String"
str2 = "Second Srting"

str3 = str1 + '' + str2
print(str3) # First StringSecond Srting

str4 = str1*3
print(str4) # First StringFirst StringFirst String

# 인덱싱
print(str1[0], str1[2], str1[4]) # F r t

#슬라이싱(slicing)
str5 = str2[2:5]
print(str5) # con
print(str2[2:])

# 연결(+) + 생략가능
str3 = str1 + '' + str2
print(str3)
str6 = 'Hello''-''World'
print(str6) # Hello-World

#문자열 개체와 정수형 객체는 + 연산을 할수 없다

name = '용택'
age = 40
# print(name + age) 요고는 불가능
print(name + str(age)) # 요고는 가능 정수형 객체를 문자열로 변수 지정??

# len[] 함수 문자의 길이를 확인
print(len(str2))

#in , not in 연산
print("S" in str2) # str2에 S가 있다  = True
print("S" not in str2) # str2에 S가 없다  = False

# 문자열 객체는 변경할수 없다 (Immutable)
#str1[0] = 'f'
#print(str1)

# Process finished with exit code 0 정상코딩
# Process finished with exit code 1 에러코딩


# formating (서식) - tuple
f = "name:%s, age:%d"
print(f)
print(f % ('지환',29))
print(f % ('은성',32))

# formating (서식) - format() 함수
name = "천웅"
age = 31
print("name:"+ name + ", age:"+str(age))
print("name:"+ name + ", age:"+format(age, "d"))
print("name:"+ format(name,"s") + ", age:"+format(age, "d"))
#f = "name:%s, age:%d"

# 대소문자 관련 객체 함수
s = "i like Python"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

#검색관련 함수

s = "i like Python, i like Java Also"
print(s.count("like"))
print(s.find("like"))
print(s.find("like",5))
print(s.find("JavaScript"))
print(s.rfind("like"))