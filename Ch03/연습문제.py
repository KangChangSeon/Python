# #LAP 4번 문제 / 205p
# def print_hash(n):
#     for i in range(n):
#         print(i,'#####')
# print_hash(6)

# def foo(m,n):
#     s=m+n
#     print(s)
# foo(3,4)

# n=5
# for i in range(0,n):
#     print(' '*i,end='')
# for k in range(5,0,-1):
#     print('*'*k)

# #*로 마름모 만들기 완성본
# n=5
# for i in range(n):
# 	print(' '*(n-(i+1)), end='')
# 	print('*'*(2*i+1))
# for i in range(n - 2, -1, -1):
#     print(' ' * (n - i - 1), end='')
#     print('*' * (2 * i + 1))

# #3.23 189p
# n = int(input('n의 값>'))
# s=0

# for i in range(1,n+1):
#     s+=(i**2)
#     print(s)


# #3.22 189p
# is_primes=[]
# val=int(input('정수 입력>'))
# for n in  range(2,val+1):
#     is_prime=True
#     for num in range(2,n):
#         if n%num==0:
#             is_prime=False
#             print(n,'= 합성수')
#             break
#     if is_prime:
#         print(n,'= 소수')

# 153 = 1**3 + 5**3 + 3**3
# Ams= n1**3 + n2**3 + n3**3

# 153/100=1(n1) - 100의자리수
# 153/10-(10*n1)=5(n2) - 10의자리수
# 153 - ((100*n1)+(n2*10))=3(n3) - 1의 자리수

# A=int(input('암스트롱 수를 구할 범위>'))
# ARR=[] #암스트롱 해당 수 리스트 포함

# def AMS(i):
#     n1=i/100
#     n2=i-(10*n1)
#     n3=i-((100*n1)+(10*n2))
#     cul=n1**3+n2**3+n3**3
#     if cul == i:
#         ARR.append(i)

# for i in range(1,A):
#     AMS(i)
# print(ARR)
# 산술 구문 실패


# #3.27p 191p
# def AMS(n):
#     n = int(n)
#     n1 = n // 100
#     n2 = (n % 100) // 10
#     n3 = n % 10
#     cul = n1 ** 3 + n2 ** 3 + n3 ** 3
#     if cul == n:
#         ARR.append(n)
# ARR=[]
# for i in range(2,500):
#     AMS(i)
# print(ARR)

# def AMS(n):
#     n1 = n // 100
#     n2 = (n % 100) // 10
#     n3 = n % 10
#     cul = n1 ** 3 + n2 ** 3 + n3 ** 3
#     if cul == n:
#         return n
#     else:
#         return None

# ARR = []
# for i in range(152,154):
#     if AMS(i) != None:
#         ARR.append(AMS(i))

# print(ARR)


# #3.18 187p
# print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다')
# print('1)햄버거')
# print('2)치킨')
# print('3)피자')

# num=0
# while num not in [1,2,3]:
#     num=int(input('1에서 3까지의 메뉴를 선택하시오>'))
#     print('잘못 입력하셨습니다.')

# if num==1:
#     print('햄버거를 선택하셨습니다.')
# elif num==2:
#     print('치킨을 선택하셨습니다.')
# else:
#     print('피자를 선택하셨습니다.')

# #3.24 189p
# n = int(input('n을 입력하시오>'))
# s=0
# for i in range(1,n+1):
#     s+=(1/i)**2
# print(s)