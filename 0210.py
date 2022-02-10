# 리스트 : 자료를 모아서 활용할 수 있게 만드는 특별한 형태의 자료. 대괄호 내부에 여러 종류의 자료를 넣어 선언하며, 선언한 리스트를 출력하면 내부의 자료를 모두 출력한다.


# 리스트 예제

array = [273, 32, 103, "Hello", True, False]
print(array)


# 요소(element) : 대괄호 내부에 넣는 자료. 각각의 요소는 인덱스로 저장된다.


# 요소 예제

list_a = [273, 32, 103, "Hello", True, False]
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[1:3])


# 리스트의 특정 요소 변경 예제

list_b = [273, 32, 103, "Hello", True, False]
list_b[0] = "World"
print(list_b[0])


# len 함수 : 괄호 내에 리스트 변수를 넣으면 요소의 개수를 세어준다.


# len 함수 예제

list_c = [273, 32, 103, "Hello", True, False]
print(len(list_c))


# in 연산자 / not in 연산자 : 특정 값이 리스트 내부에 있는지 확인하는 연산자.


# in 연산자 예제

list_d = [273, 32, 103, 57, 52]
print(273 in list_d)
print(99 in list_d)


# not in 연산자 예제

list_e = [273, 32, 103, 57, 52]
print(273 not in list_e)
print(99 not in list_e)


# for 반복문 : 컴퓨터에 반복을 지시하는 방법


# for 반복문 예제

array = [273, 32, 103, 57, 52]
for element in array :
  print(element)


# for 반복문과 문자열 예제

for character in "Hello" :
  print(character)


# 리스트에 적용할 수 있는 함수 : min(), max(), sum() .


# 리스트 적용 함수 예제

numbers = [103, 52, 273, 32, 77]
print(min(numbers))
print(max(numbers))
print(sum(numbers))