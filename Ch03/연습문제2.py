# #3.2
# name=input('이름을 입력하시오 : ')
# height=int(input('키를 입력하시오(단위 cm) : '))

# if height>=140:
#     print(name,'님은 놀이기구를 탈 수 있습니다.')
# else:
#     print(name,'님은 놀이기구를 탈 수 없습니다.')

# #3.4
# age=int(input('나이를 입력하시오 : '))

# if age>=20:
#     print('Adult')
# elif age<20 and age>=10:
#     print('Youth')
# else:
#     print('Kid')

# #3.5
# n1,n2=(input('두 정수를 입력하시오>').split())

# if n1>n2:
#     print(n2,n1)
# else:
#     print(n1,n2)

# #3.9
# num=int(input('정수를 입력하시오 : '))

# if num%2==0 and num%3==0:
#     print(num,'은 2로 나누어집니다.')
#     print(num,'은 3으로 나누어집니다.')
#     print(num,'은 2와 3 모두로 나누어집니다.')
# elif num%2==0 and num%3!=0:
#     print(num,'은 2로 나누어집니다.')
#     print(num,'은 3으로 나누어지지 않습니다.')
#     print(num,'은 2와 3 모두로 나누어지지 않습니다.')
# elif num%2!=0 and num%3==0:
#     print(num,'은 2로 나누어지지 않습니다.')
#     print(num,'은 3으로 나누어집니다.')
#     print(num,'은 2와 3 모두로 나누어지지 않습니다.')
# else:
#     print(num,'은 2로 나누어지지 않습니다.')
#     print(num,'은 3으로 나누어지지 않습니다.')
#     print(num,'은 2와 3 모두로 나누어지지 않습니다.')

# #3.10
# a,b = map(int,input("값을 입력하세요 :").split())

# if a%b==0:
#     print('{}는 {}의 배수입니다.'.format(a,b))
# else:
#     print('{}는 {}의 배수가 아닙니다.'.format(a,b))

# #3.11
# n1,n2,n3 = map(int,input('세 복권번호를 입력하시오 : ').split())
# n=0
# a,b,c=(2,3,9)

# if n1==n2 or n2==n3 or n1==n3:
#     print('잘못된 복권 번호입니다.')
#     exit()
# if n1==2 or n1==3 or n1==9:
#     n+=1
# if n2==2 or n2==3 or n2==9:
#     n+=1
# if n3==2 or n3==3 or n3==9:
#     n+=1

# if n==0:
#     print('다음 기회에...')

# elif n==1:
#     print('1만원')

# elif n==2:
#     print('1천 만원')

# else:
#     print('1억원')


# #3.14
# i=(input('알파벳을 입력하시오 : '))

# if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#     print(i,'는 모음입니다.')
# else :
#     print(i,'는 자음입니다.')

#3.15
# #for 문
# n=2
# for i in range(1,10):
#     print('{}*{}={}'.format(n,i,n*i))

# #while 문
# n=2
# i=1
# while(1):
#     print('{}*{}={}'.format(n,i,n*i))
#     i+=1
#     if i>=10:
#         break



# #3.16
# #for문
# n=int(input('1에서 9까지의 수를 입력하세요 : '))
# if n>9 or n<1:
#     n=int(input('1에서 9까지의 수를 다시 입력하세요 : '))
    
# for i in range(1,10):
#     print('{}*{}={}'.format(n,i,n*i))


# #while문
# n=0
# i=0
# while n not in (1,2,3,4,5,6,7,8,9):
#     n=int(input('1에서 9까지의 수를 입력하세요 : '))
#     continue
# while(1):
#     print(n,'*',i,'=',n*i)
#     i+=1
#     if i>9:
#         break

# #3.18
# print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
# print('1)햄버거')
# print('2)치킨')
# print('3)피자')

# menu=int(input('1에서 3까지의 메뉴를 선택하세요 : '))
# while menu<1 or menu>3:
#     menu=int(input('메뉴를 다시 입력하세요 : '))
#     continue
# if menu==1:
#     print('햄버거를 선택하였습니다.')
# elif menu==2:
#     print('치킨을 선택하였습니다.')
# else:
#     print('피자를 선택하였습니다.')

# #3.19
# print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
# print('햄버거(입력 b)')
# print('치킨(입력 c)')
# print('피자(입력 p)')

# menu=input('메뉴를 선택하세요(알파벳 b,c,p 입력) : ')
# while menu not in ('b','c','p'):
#     menu=input('메뉴를 다시 입력하세요 : ')
#     continue
# if menu=='b':
#     print('햄버거를 선택하였습니다.')
# elif menu=='c':
#     print('치킨을 선택하였습니다.')
# else:
#     print('피자를 선택하였습니다.')

# #3.20

# num = int(input('숫자를 입력하세요 : '))

# for i in range(1, num + 1) :     
#     print (' ' * (num - i) + '*' * i)

# #3.22
# for i in range(2, 13) :
#     flag = True
#     for j in range(2, i) :
#         if i % j == 0 :
#             flag = False
#             break
#     if flag :
#         print(i, ': 소수')
#     else:
#         print(i, ': 합성수')

# #4.1
# def my_greet():
#     print('환영합니다.')
# my_greet()
# my_greet()

# #4.2
# def square(n):
#     return n**2

# print('3의 제곱은 : ',square(3))
# print('4의 제곱은 : ',square(4))

##4.3
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

# #4.4
# def mile2km(m):
#     for i in range(1,m+1):
#         print('{} 마일 = {} 킬로미터'.format(i,i*1.61))

# mile2km(5)

# #4.9 내가 한거
# def mean_of_n(*nums):
#     s=0
#     for i in nums:
#         s+=i
#         print(s/len(nums))

# def max_of_n(*nums):
#     s=0
#     for i in nums:
#         if i>s:
#             s=i
#     print(s)

# def min_of_n(*nums):
#     s=0
#     for i in nums:
#         if i<s:
#             s=i
#     print(s)

# nums=map(int,input('정수를 여러 개 입력하시오 : ').split())
# mean_of_n(nums)
# max_of_n(nums)
# min_of_n(nums)

# #4.9 정답
# def mean_of_n(*nums):
#     s = sum(nums)
#     print(('{:.1f}').format(s / len(nums)))

# def max_of_n(*nums):
#     s = nums[0]
#     for i in nums:
#         if i > s:
#             s = i
#     print(s)

# def min_of_n(*nums):
#     s = nums[0]
#     for i in nums:
#         if i < s:
#             s = i
#     print(s)

# nums = list(map(int, input('정수를 여러 개 입력하시오 : ').split()))
# mean_of_n(*nums)
# max_of_n(*nums)
# min_of_n(*nums)


