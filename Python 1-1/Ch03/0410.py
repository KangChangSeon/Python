# for i in range(5):
#     for k in range(5,i,-1):
#         print(' ',end='')
#     for k in range((i+1)*2-1):
#         print('*',end='')
#     print()

# n=5
# for i in range(n):
#     for j in range(n-(i+1)):
#         print(' ',end='')
#     for j in range(2*i+1):
#         print('*',end='')
#     print()

# n=5
# for i in range(n):
# 	print(' '*(n-(i+1)), end='')
# 	print('*'*(2*i+1))

# i=10
# while(1):
#     print("Hello Pyrhon")
#     i-=1
#     if i<0:
#         break

# i=10
# while(i>=0):
#     if i%2==0:
#         i-=1
#         continue
#     print(i,'hello')
#     i-=1

# p1 = input(str('가위 바위 보 중에 선택>'))
# p2 = input(str('가위 바위 보 중에 선택>'))
# p1=''
# p2=''
# while p1 not in ['가위','바위','보'] or p2 not in ['가위','바위','보']:
#     p1=input(str('가위,바위,보 중에 선택>'))
#     p2=input(str('가위,바위,보 중에 선택>'))

# # while p2 not in ['가위','바위','보']:
# #     p2=input(str('가위,바위,보 중에 선택>'))
    
# if p1==p2:
#     print('무승부')
# if p1 == '가위':
#     if p2=='바위':
#         print('p2 승리')
#     else:
#         print('p1 승리')

# elif p1 == '바위':
#     if p2 =='가위':
#         print('p1 승리')
#     else:
#         print('p2 승리')

# else:
#     if p2 =='가위':
#         print('p1 승리')
#     else:
        # print('p2 승리')

# def print_star():
# 	print('*****')
# print_star()

# def print_star(n):
# 	for _ in range(n):
# 		print('*****')
# print_star(4)

