# print('Hello World')

# name = 'KANG'
# addr = 'BUSAN'
# print(name, addr)

# name = input('name : ')
# print('your name : ', name)

# x = int(input('number 1 : '))
# y = int(input('number 2 : '))
# print(f'result is {x}+{y} = {x+y}') ##f' string 활용

# #문제 풀이/아메리카노는 1500원 카푸치노 5000원 카페라떼 4000원, 2잔씩 토탈 계산
# ame = 1500
# capu = 5000
# latte = 4000
# print(f'Total result : {(ame+capu+latte)*2}')

# #리스트
# x = [0,0,0,0]
# x[0] = int(input('score 1 : '))
# x[1] = int(input('score 2 : '))
# x[2] = int(input('score 3 : '))
# x[3] = int(input('score 4 : '))
#
# hap = x[0] + x[1] + x[2] + x[3]
#
# print('result : ', hap)
# #리스트 대괄호([ ]) 안에 서로 다른 자료형의 값을 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형
# #대괄호([ ])에 넣는 자료를 요소(element)라고 부르며, 요소들은 순서를 가지고 있고 인덱스를 사용하여 참조할 수 있음


# #튜플
# #튜플은 한번 저장된 값은 수정할 수 없는 자료형으로 읽기 전용의 데이터를 저장할 때 유용하게 사용함
# x = ()
# print(x)
# x = (1,2,3)
# print(x)
# #데이터 변경은 오류 발생으로 불가능

# #딕셔너리
# #딕셔너리는 순서가 없는 컬렉션 자료형으로 각각의 요소는 key:value 형태로 저장
# #딕셔너리는 리스트나 튜플처럼 인덱스에 의해 해당 요소를 찾지 않으며, key를 통해 value를 얻음
# menu = {'김밥':3000, '라면':5000}
# print(menu['김밥'])
# print(menu)
# >3000
# >{'김밥': 3000, '라면': 5000}

# #세트
# #세트는 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형으로 중복을 허용하지 않는 컬렉션 자료형
# #세트 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없음
# x = {10,20,30}
# print(x)
# y = set([10,20,30])
# print(y)
# x = {10,20,30,20}
# print(x)
# >{10, 20, 30}
# >{10, 20, 30}
# >{10, 20, 30}

# #세트 연산
# #교집합
# x = {10,20}
# y = {20,30}
# print(x&y)
# print(x.intersection(y))
#
# #합집합
# print(x|y)
# print(x.union(y))
#
# #차집합
# print(x-y)
# print(x.difference(y))

