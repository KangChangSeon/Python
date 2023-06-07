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

src = str(input('문자열을 입력하시오: '))
tmp = src[0]

result = ''
result2 = ''
num = 0

if src.strip() == '':
    output = ''
    print('src = {}'.format(src))
    print('output = {}'.format(output))

else:
    for i in src:
        if i == tmp:
            num += 1
        elif i != tmp:
            result += tmp + str(num)
            tmp = i
            num = 1

    result += tmp + str(num)

    for j in range(0, len(result), 2):
        result2 += (result[j] * int(result[j+1]))

    print('src = {}'.format(src))
    print('output = {}'.format(result))
    print('output2 = {}'.format(result2))
