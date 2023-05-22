# a_list = [10,20,30,40,50,60,70,80]
# i = 0

# for n in a_list:
# 	print(a_list[i])
# 	i = i + 1
# 	#print(n) 이렇게 해도 n = 인덱스의 값으로 해서 똑같이 출력됨.


##슬라이싱과 스텝
# a_list = [10,20,30,40,50,60,70,80]

# print(a_list[1:])
# print(a_list[-7:-2])
# print(a_list[-7:])
# print(a_list[:-2])
# print(a_list[-2:])
# print(a_list[:])
# print(a_list[:-2]+a_list[-2:])
# print(a_list[-2:]+a_list[:-2])

# a_list = [10,20,30,40,50,60,70,80]

# print(a_list[0:8:3])
# print(a_list[::-1]) #전체를 다 들고 오는데 역순으로 들고 와라 (-1 = 역순)

# #딕셔너리 자료형

# person = {'이름':'홍길동', '나이':26, '몸무게':82}

# print(person['이름'])
# print(person['나이'])
# print(person['몸무게'])

# capital_dic = {'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}

# print(capital_dic['Korea'])
# print(capital_dic['China'])
# print(capital_dic['USA'])

# d1 = {'이름':'홍길동','나이':26}
# d2 = {'나이':26, '이름':'홍길동'}
# print(d1==d2)

# capital_dic = {'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}

# print('Korea' in capital_dic)
# print('China' in capital_dic)
# print('Indonesia' in capital_dic)
# print('Beijing' in capital_dic)

# person = {'이름':'홍길동', '나이':26, '몸무게':82}

# print(person.keys())
# print(person.values())
# print(person.items())
# print(person.get('취미'))
# print(person.get('이름'))
# print(person.popitem())
# print(person.pop('나이'))
# print(person.clear())

# print(person)

# person = {'이름':'홍길동', '나이':26, '몸무게':82}

# for key in person:
#     print('{}:{}'.format(key,person[key]))


# fruits_dic = {'apple':6000, 'melon':3000, 'banana':5000, 'orange':7000}

# for key in fruits_dic:
#     print('{}:{}'.format(key,fruits_dic[key]))

# print(fruits_dic.keys())
# print(fruits_dic.values())
# print(fruits_dic.pop('apple'))
# print(fruits_dic)
# print(fruits_dic.clear())
# print(fruits_dic)

# #LAB 6-5
# fruits_dic = {'apple':6000, 'melon':3000, 'banana':5000, 'orange':7000}

# fruits_keys = []

# for key in fruits_dic:
#     fruits_keys.append(key)

# print(fruits_keys)

# a = 100
# b = 200
# print('swap 이전 : a = {}, b = {}'.format(a,b))

# a,b = b,a
# print('튜플을 사용한 swap 결과 : a = {}, b = {}'.format(a,b))

# t0 = (10,20,30)
# t1 = t0 + t0

# print(t1)

# t2 = t0 * 2

# print(t2)

# t3 = t0 + 40

# print(t3)

# t4 = t0 + (40,)

# print(t4)

# t = (10,20,30,20,20,10,50)

# print(t.count(10))
# print(t.index(30))

# t_fruits = ('apple', 'orange', 'water-melon')
# print('변경전 :',t_fruits)

# f_list = list(t_fruits)
# f_list[1] = 'kiwi'

# t_fruits = tuple(f_list)
# print('변경후 :', t_fruits)

# def area_and_circum(radius):
#     area = 3.14 * radius ** 2
#     circum = 2 * 3.14 * radius
#     return area, circum

# r = 4
# a,c = area_and_circum(r)
# print('반지름 {}인 원의 면적과 둘레 : {} , {}'.format(r,a,c))

# def square(x,y):
#     return x ** 2, y ** 2

# x = 10
# y = 20
# x_sq, y_sq = square(x,y)

# print('{} 제곱 = {}, {} 제곱 = {}'.format(x,x_sq,y,y_sq))

# s = {100,100,200,200,300,400}
# print(s) #중복 원소를 제외하고 출력

# s.add(500) #원소 500을 추가
# print(s)

# s.discard(100) #원소 100을 삭제
# print(s)


# s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}

# print(s1|s2)
# print(s1.union(s2))

# print(s1&s2)
# print(s1.intersection(s2))

# print(s1-s2)
# print(s1.difference(s2))

# print(s1^s2)
# print(s1.symmetric_difference(s2))

# #합집합
# s1 | s2 = {1,2,3,4,5,6,7,8,9} or s1.union(s2)

# #교집합
# s1 & s2 = {4,5,6} or s1.intersection(s2)

# #차집합
# s1 - s2 = {1,2,3) or s1.difference(s2)

# #대칭 차집합
# s1 ^ s2 = {1,2,3,7,8,9} or s1.symmetric.difference(s2)