# def max2(m,n):
#     if m>n:
#         return m
#     else:
#         return n

# def min2(m,n):
#     if m>n:
#         return n
#     else:
#         return m
# print('100과 200중 큰 수는 :',max2(100,200))
# print('100과 200중 작은 수는 :',min2(100,200))


# #5.3
# list1 = [3,5,7]
# list2 = [2,3,4,5,6]

# for i in list1:
#     for j in list2:
#         print("{} * {} = {}".format(i,j,i*j))


# list1 = [3,5,7]
# list2 = [2,3,4,5,6]

# for i in range(len(list1)):
#         for j in range(len(list2)):
#             print(list1[i]*list2[j])


# #5.4
# a = [2, 3, 4, 5, 6]
# rev_a = []

# while a:
#     rev_a.append(a.pop())

# print(rev_a)


# #5.5
# list1 = ['I like','I love']
# list2 = ['pancakes','kiwi juice','espresso']

# for i in list1:
#     for j in list2:
#         result = list1[list1.index(i)]+" "+list2[list2.index(j)]
#         print(result)

# #5.7
# # n_list = [10,20,30,50,60]
# # # print(sum(n_list))

# # for i in n_list:
# #     sum = []
# #     sum += n_list[n_list.index(i)]
# # print(sum)

# n_list = [10, 20, 30, 50, 60]
# # print(sum(n_list))

# # sum 변수를 리스트로 사용하는 것은 좋지 않습니다. sum 함수와 겹칠 수 있고, 값을 누적할 수 없습니다.
# # 따라서 sum 변수를 사용하지 않고, 다른 변수를 사용하여 값을 누적합니다.
# total = 0

# for i in n_list:
#     # sum 변수를 리스트로 초기화하는 것은 매번 반복할 때마다 새로운 빈 리스트로 초기화하는 것을 의미합니다.
#     # 그러면 매번 누적된 값들이 사라지므로, 원하는 결과를 얻을 수 없습니다.
#     # 대신에 sum 변수를 사용하지 않고, 누적된 값을 total 변수에 더해주어야 합니다.
#     total += i

# print(total)


#5.8

# n_list = [10,20,30,50,60]

# for i in n_list:
#     total = n_list[n_list.index(i)] * n_list[n_list.index(i+1)]

# print(total)

# n_list = [10, 20, 30, 50, 60]

# total = 1

# for i in n_list:
#     total *= i

# print(total)


## 5.9
# n_list = [10,20,30,50,60]

# min_num = n_list[0]
# max_num = n_list[0]

# for i in n_list:
#     if min_num > n_list[n_list.index(i)]:
#         min_num = n_list[n_list.index(i)]

# # for i in range(len(n_list)):
# #     if min_num > n_list[i]:
# #         min_num = n_list[i]

# print(min_num)

# for i in n_list:
#     if max_num < n_list[n_list.index(i)]:
#         max_num = n_list[n_list.index(i)]

# # for i in range(len(n_list)):
# #     if max_num < n_list[i]:
# #         max_num = n_list[i]

# print(max_num)



# # 5.11
# numbers = list(map(int, input("수를 입력하세요: ").split()))

# sum = 0
# max = numbers[0]
# min = numbers[0]

# for i in range(len(numbers)):
#     sum += numbers[i]

# avg = sum / len(numbers)

# for i in range(len(numbers)):
#     if max < numbers[i]:
#         max = numbers[i]


# for i in range(len(numbers)):
#     if min > numbers[i]:
#         min = numbers[i]

# print("합계 : {}".format(sum))
# print("평균 : {}".format(avg))
# print("최댓값 : {}".format(max))
# print("최솟값 : {}".format(min))




# src = (str(input('문자열을 입력하시오')))
# tmp = src[0]


# num = 0

# for i in src:
#     if i == tmp:
#         num += 1

#     elif i != tmp:
#         s = num
#         print(tmp,num)
#         tmp = i
#         num = 1

# print(tmp,num)

# src = str(input('문자열을 입력하시오: '))
# tmp = src[0]

# result = ''
# result2 = ''
# num = 0

# if src == '':
#     print("src = ''")
#     print("output = ''")

# else:
#     for i in src:
#         if i == tmp:
#             num += 1
#         elif i != tmp:
#             result += tmp + str(num)
#             tmp = i
#             num = 1

#     result += tmp + str(num)

#     for j in range(0,len(result),2):
#         result2 += (result[j]*int(result[j+1]))

#     print('src = {}'.format(src))
#     print('output = {}'.format(result))
#     print('output2 = {}'.format(result2))

# src = str(input('문자열을 입력하시오: '))
# tmp = src[0]

# result = ''
# result2 = ''
# num = 0

# if src.strip() == '':
#     output = ''
#     print('src = {}'.format(src))
#     print('output = {}'.format(output))

# else:
#     for i in src:
#         if i == tmp:
#             num += 1
#         elif i != tmp:
#             result += tmp + str(num)
#             tmp = i
#             num = 1

#     result += tmp + str(num)

#     for j in range(0, len(result), 2):
    #     result2 += (result[j] * int(result[j+1]))

    # print('src = {}'.format(src))
    # print('output = {}'.format(result))
    # print('output2 = {}'.format(result2))



# capital = {'Korea' : 'Seoul', 'China' : 'Beijing', 'USA': 'Washington'}
# print(capital['Korea'])
# capital['Japan'] = 'Tokyo'
# print(capital['Japan'])

# del capital['Japan']
# # print(capital['Japan']) #error


# # print(capital.keys())
# # print(capital.values())
# # print(capital.items())

# # print(capital.get('USA'))

# for key in capital:
#     print("{} : {}".format(key,capital[key]))


# fruits = {'apple': 6000, 'melon' : 3000, 'banana':5000,'orange':4000}
# print(fruits.keys())
# print(fruits.values())
# print(len(fruits))

# a = (1,2,3)

# print(a)
# d,c,e = a
# print(d,c,e)

# d = c
# print(d,c,e)


# the_day = (1919,3,1)

# year, month, day = the_day
# print("{}년 {}월 {}일은 삼일절입니다.".format(year,month,day))

# list1 = [10,20,30]
# tuple1 = tuple(list1)

# a,b,c, = tuple1
# print(a,b,c)

# t = (10,20,10,30,40)

# print(t.index(10))

# person = (2019001,'홍길동',179)

# print(person)

# person_l = list(person)

# person_l[0] = 2020003


# person = tuple(person_l)

# print(person)


# x = (int(input('x')))
# y = (int(input('y')))

# def square(x,y):
#     x = x**2
#     y = y**2
#     return x,y
# x_sq, y_sq = square(x,y)
# print('{} 제곱 {}, {} 제곱 {}'.format(x,x_sq,y,y_sq))

# print('hello'*3)
# print(('hello',)*3)


# menu = {'Americano':3000,'Ice Americano':3500,'Cappuccino':4000,'Cafe Latte':4500,'Espresso':3600}

# for key in menu:
#     print("{:13s} 가격 : {}".format(key, menu[key]))

# choice = (str(input("위의 메뉴중 하나를 선택하세요 : ")))

# if choice in menu.keys():
#     print('{}는 {}원 입니다. 결제를 부탁드립니다.'.format(choice,menu.get(choice)))
# else:
#     print('미안합니다. {}는 메뉴에 없습니다.'.format(choice))

# result = (100,121,120,130,140,120,122,123,190,125)



# for i in range(len(result)):
#     x = result[i]
#     i+=1
#     if x > result[i]:
#         print("지난 {}일 동안 전일대비 매출이 감소한 날은 {}일입니다.".format(len(result),i+1))
#         if i >= 9:
#             break
        
# #6.15
# n = (4,5,2,3,8,1,9,0)

# print(n)

# for i in range(len(n)):
#     if i == 0:
#         continue
#     print(n[0:-i])


# n = (1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)

# n_l = list(n)
# result = list(n)
# answer = []

# print(n_l)

# for i in range(len(n)):
#     for j in range(len(result)):
#         if n_l[i] == result[j]:
#             answer.append(i)

    
# print(answer)

# n = (1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)

# n_l = list(n)
# result = list(n)
# answer = []

# print(n_l)

# for i in range(len(n)):
#     for j in range(i + 1, len(result)):
#         if n_l[i] == result[j] and n_l[i] not in answer:
#             answer.append(n_l[i])

# print(answer)

# n = (1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)

# n_l = list(n)
# result = list(n)
# answer = []

# print(n_l)

# for i in range(len(n)):
#     count = 0
#     for j in range(len(result)):
#         if n_l[i] == result[j]:
#             count += 1
#         if count > 1 and n_l[i] not in answer:
#             answer.append(n_l[i])
#             break

# print(answer)

