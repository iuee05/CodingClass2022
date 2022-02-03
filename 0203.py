# ' % ' 나머지연산 . 나머지의 값을 출력하는 기호


# 복합 대입 연산자 : 자료형에 적용하는 기본 연산자와 ' = ' 연산자를 함께 사용해 구성 . += , -= , *= , /= , %= , **= .


# 복합 대입 연산자 예제

number = 100
number += 10
print (number)

number = 100
number += 10
number += 20
number += 30
print (number)

# 문자열 복합 대입 연산자 예제

string = "hello"
string += "!"
print (string)


# Boolean 자료형 : Boolean ( Bool ) 은 참과 거짓을 판단하는 자료형으로 true 또는 false 값만 가진다.


# Bool 자료형 비교 연산자 : == , != , > , < , >= , <= .


# Bool 자료형 예제

print (10 == 100)
print (10 != 100)
print (10 > 100)
print (10 < 100)
print (10 >= 100)
print (10 <= 100)


# if 조건문 : 조건에 따라 코드를 실행하거나 실행하지 않을 때 사용하는 구문. 코드의 실행 흐름 변경


# if 조건문 예제

# 입력받기
number = input("정수 입력 > ")
number = int(number)

# 양수 조건
if number > 0 :
  print ("양수입니다.")

# 음수 조건
if number < 0 :
  print ("음수입니다.")

# 0 조건
if number == 0 :
  print ("0입니다.")


# 나머지 연산자 활용 _ 짝수와 홀수 구분


# 나머지 연산자 활용 예제

# 입력받기
number = input("정수 입력 > ")
number = int(number)

# 짝수 조건
if number % 2 == 0 :
  print ("짝수입니다.")

# 홀수 조건
if number % 2 == 1 :
  print ("홀수입니다.")


# else 구문 : if 조건문 뒤에 사용하는, 조건이 거짓일 때 실행되는 부분.


# else 구문 예제

number = input ("정수 입력 > ")
number = int(number)

if number % 2 == 0 :
  print ("짝수입니다.") #조건이 참일 때, 즉 짝수 조건

else :
  print ("홀수입니다.") #조건이 거짓일 때, 즉 홀수 조건


#elif 구문 : 세 개 이상의 조건을 연결할 때 사용하는 구문. if 조건문과 else 구문 사이에 입력


# elif 구문 예제

num = int(input('0 ~ 100 안에서 숫자 하나를 입력해 주세요 : '))

if num < 10 :
  print ('입력값은 10보다 작습니다.')
elif num > 10 and num <= 50 :
  print ('입력값은 10보다 크고 50보다 작거나 같습니다.')
elif num >51 and num <= 100 :
  print ('입력값은 51보다 크고 100보다 작거나 같습니다.')
else :
  print ('입력값이 범위 내에 포함되지 않습니다.')