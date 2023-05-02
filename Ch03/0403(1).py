# grade=int(input("성적을 입력하시오>"))

# if grade>=90:
#     print('A')
# elif grade>=80:
#     print('B')
# elif grade>=70:
#     print('C')
# elif grade>=60:
#     print('D')
# else:
#     print('F')

# speed=int(input("자동차의 속도(km/h)를 입력하시오>"))

# if speed >= 100:
#     print("고속")
# elif speed >=60:
#     print("중속")
# else:
#     print("저속")

# for i in range(5):
# 	print(i, end='')

# s=0
# for i in range(1,11):
#     s+=i
# print('1부터 10까지의 합=',s)

# s=0
# for i in range(1, 101, 2):
#     s+=i
#     print('i={}, s={}'.format(i,s))
# print()
# print('1부터 100까지 홀수의 합=',s)

# n=int(input('합계를 구할 수를 입력>'))
# s=0
# for i in range(0,n):
# #for i in range(1, n+1)
#     s=s+(i+1)


# n=int(input('구구단 정수>'))
# for i in range(1,10):
#     gugudan=n*i
#     print(n,'*',i,'=',gugudan)


# for i in range(2,10):
#     for j in range(1,10):
#         print(i,'*',j,'=',i*j)
#     print()

# n=7
# for i in range(n):
#     print(' '*i+'#')

# n=7
# for i in range(n):
#     st=''
#     for j in range(i):
#         st=st+' '
#     print(st+'#')

# for i in range(6, -1, -1):
#     st=''
#     for j in range(i):
#         st = st+' '
#     print(st+'#')

# n=5
# for i in range(n):
#     st=''
#     sk=''
#     for j in range(n-(i+1)):
#         st=st+' '
#     for k in range(i):
#         sk=sk+'*'+'*'
#     print(st+sk+'*')

# for i in range(5):
#     for k in range(5,i,-1):
#         print(' ',end='')
#     for k in range((i+1)*2-1):
#         print('*',end='')
#     print()

# n=7
# for i in range(n,-1,-1):
#     st=''
#     for j in range(i):
#         st = st+' '
#     print(st+'#')

# txt='강아지 이름은 \'체리\' 이다'
# print(txt)