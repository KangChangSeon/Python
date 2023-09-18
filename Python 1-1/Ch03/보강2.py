##2.3
# width = 30
# height = 60
# area = width*height
# print('사각형의 면적=',area)

# #2.4
# width = 40
# height = 20
# area = width*height/2
# print('삼각형의 면적=',area)

# #2.5
# width=int(input('밑변의 길이를 입력하시오>'))
# area=width*width
# print('정사각형의 면적 = ',area)

# #2.6
# print('1에서 10까지의 합 =', 1+2+3+4+5+6+7+8+9+10)
# #2.7
# print('10! =', 1*2*3*4*5*6*7*8*9*10)

# #2.8
# print('a\tn\ta**n')
# print('2\t2\t',2**2)
# print('3\t2\t',3**2)
# print('4\t2\t',4**2)
# print('5\t2\t',5**2)
# print('6\t2\t',6**2)

# #2.9
# print('섭씨\t화씨')
# print('0\t',(9/5)*0+32)
# print('10\t',(9/5)*10+32)
# print('20\t',(9/5)*20+32)
# print('30\t',(9/5)*30+32)
# print('40\t',(9/5)*40+32)
# print('50\t',(9/5)*50+32)

# #2.10
# celsius=int(input('섭씨 온도를 입력하세요 : '))
# fahrenheit=(9/5)*celsius+32
# print('섭씨',celsius,'도는 화씨',fahrenheit,'도 입니다.')

# #2.12
# radius=11
# PI=3.141592
# circum = 2*PI*radius
# area = PI * radius * radius
# print('원의 반지름 =',circum)
# print('원의 둘레 =',area)

# #2.13
# radius=int(input('원의 반지름을 입력하세요 >'))
# PI=3.141592
# circum = 2*PI*radius
# area = PI * radius * radius
# print('원의 반지름 =',circum)
# print('원의 둘레 =',area)

# #2.14
# print('2의 제곱근 =', 2**0.5)
# print('3의 제곱근 =', 3**0.5)
# print('4의 제곱근 =', 4**0.5)
# print('5의 제곱근 =', 5**0.5)
# print('6의 제곱근 =', 6**0.5)
# print('7의 제곱근 =', 7**0.5)
# print('8의 제곱근 =', 8**0.5)
# print('9의 제곱근 =', 9**0.5)
# print('10의 제곱근 =', 10**0.5)

# #2.15
# width=int(input('밑변을 입력하시오 >'))
# height=int(input('높이를 입력하시오 >'))
# hypon=(width**2 + height**2) ** 0.5
# print(hypon)

# #2.16 (1)
# position=1+2j
# print('회전하기전 : ',position)
# rotation=0+1j #cos90도는 0, sin90도는 1
# print('90도 회전한 후 : ',rotation*position) #회전시키는 방법 : cos a+ (sin a)i

# #2.16 (2)
# position=1+2j
# print('회전하기전 : ',position)
# rotation=((3**0.5) / 2 + 0.5j) #cos30도는 루트3/2 이며 sin30도는 1/2 이다
# print('30도 회전한 후 : ',rotation*position)

# #2.17
# print(2<<0, 2<<1, 2<<2, 2<<3, 2<<4, 2<<5, 2<<6, 2<<7, 2<<8, 2<<9)

# #2.18
# n=int(input('정수를 입력하세요 >'))
# print('이 수가 짝수인가요?', n%2==0)

# #2.19
# n=int(input('정수를 입력하세요 > '))
# print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?',(0<=n and n<=100) and n%2==0)
# n=int(input('정수를 입력하세요 > '))
# print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?',(0<=n and n<=100) and n%2==0)

# #2.22
# a=int(input('정수 a를 입력하시오 > '))
# b=int(input('정수 b를 입력하시오 > '))
# print('a/b의 몫',a//b)
# print('a/b의 나머지',a%b)

# #2.23
# n=int(input('세자리 정수를 입력하시오 > '))
# print('백의 자리 : ',n//100)
# print('십의 자리 : ',n//10%10)
# print('일의 자리 : ',n%10)

# #2.24
# n=int(input('세자리 정수를 입력하시오 > '))
# print(n%10)
# print(n//10%10)
# print(n//100)