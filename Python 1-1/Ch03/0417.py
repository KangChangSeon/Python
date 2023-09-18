# #LAB 4-6
# def print_area(width, height):
#     # print('밑변',width,', 높이',height,'인 삼각형의 면적은 :',int(width*height/2))
#     print('밑변 {}, 높이 {} 인 삼각형의 면적은 {}'.format(width,height,int(width*height/2)))

# print_area(10,20)

# def get_s(a,b):
#     # result=a+b
#     # return result
#     return a+b

# n1 = get_s(10,20)
# print(n1)

# n2=get_s(100,200)
# print(n2)

# def get_plus_minus(a,b):
#     return a+b, a-b

# i,j=get_plus_minus(10,20)
# print(i,j)

# def circle_area_circum(radius):
#     area = 3.14 * radius * radius
#     circum = 2 * 3.14 * radius
#     return area,circum

# radius=10
# i,j=circle_area_circum(radius)
# print('반지름 {}인 원의 면적은 {}, 원의 둘레는 {:.1f}'.format(radius,i,j))
# print('반지름',radius,'인 원의 면적은',i,'원의 둘레는 : ',round(j,2))

# def print_sum():
#     global a,b
#     a=100
#     b=200
#     result=a+b
#     print('내부 {}와 {}의 결과 값은 : {}'.format(a,b,result))

# a=10
# b=20
# print_sum()
# result=a+b
# print('외부 {}와 {}의 결과 값은 : {}'.format(a,b,result))

##인자값 할당 방식
# def print_star(n=1):
#     for i in range(n):
#         print('*****')

# print_star(5)

# def div(a,b=2):
#     #디폴트 값은 가장 마지막 부터 수행해야 한다.
#     result=a/b
#     print('{}와 {}의 나눗셈 결과 : {}'.format(a,b,result))

# div(6)
# div(8)

# def greet(*names):
#     for name in names:
#         print('안녕하세요', name,'씨')

# greet('홍길동','양만춘','이순신')
# greet('James','Thomas')

# def foo(*args):
#     print('인자의 개수 :',len(args))
#     print('인자들 :',args)

# foo(10,20,30)

# def sum_nums(*numbers):
#     result=0
#     for n in numbers:
#         result+=n
#     return result

# print(sum_nums(10,20,30))
# print(sum_nums(10,20,30,40,50))

