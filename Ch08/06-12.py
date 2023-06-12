# try:
#     a,b = input('두 수를 입력하시오').split()
#     result = int(a) / int(b)
#     print('{}/{} = {}'.format(a,b,result))
# except:
#     print('수가 정확한지 확인하시오')

# try:
#     b = 2/0
#     a = 1 +'hundred'
# except ZeroDivisionError:
#     print('0으로 나누는 오류')
# except TypeError:
#     print('지원되지 않은 연산자를 사용하는 오류')

# try:
#     a,b = input('두수를 입력하시오').split()
#     result = int(a)/int(b)
# except ZeroDivisionError:
#     print('오류 : 0으로 나눔을 시도했음')
# except ValueError:
#     print('오류 : 입력값이 정수나 실수가 아님')
# except:
#     print('오류 : 10 2 와 같이 두 정수를 입력하시오')
# else:
#     print('{} / {} = {}'.format(a,b,result))

# #LAB 8-4(1)
# f=open('number.txt','w')

# f.write('100\n')
# f.write('200\n')
# f.write('300\n')
# f.write('400\n')

# f.close()

# f = open('hello.txt','r')
# s = f.read(5)
# print(s)
# f.close()


# f = open('foo.txt','w')
# f.write('AAA\n')
# f.write('BBB\n')
# f.write('CCC\n')
# f.close()

# f = open('foo.txt','r')
# s = f.read(5)
# print(s)
# f.close()


# #LAB 8-5(1)
# f = open('number.txt','r')
# s = f.readline().rstrip()
# print(s)
# s = f.readline().rstrip()
# print(s)
# s = f.readline().rstrip()
# print(s)
# s = f.readline().rstrip()
# print(s,end='')
# f.close()

# f = open('foo.txt','a+')
# f.write('This will be appended.\n')
# f.write('This too\n')
# f.close()

# f = open('data5.txt','w')
# for _ in range(5):
#     n = input('정수를 입력하세요 : ')
#     f.write(n)
#     f.write('\n')
# f.close()

# f = open('data5.txt','r')
# su = 0
# for _ in range(5):
#     n = int(f.readline())
#     su += n

# print('다섯 숫자의 합 = {} , 평균 = {}'.format(su,su/5))
# f.close()


# def divide(x,y):
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         print('0으로 나누는 오류 발생')
#     else:
#         print('결과 :',result)
#     finally:
#         print('수행 완료')

# print('divide(100,2) 함수호출:')
# divide(100,2)
# print('divide(100,0) 함수호출:')
# divide(100,0)

# def get_ans(ans):
#     if ans in ['예','아니오']:
#         print('정상적인 입력입니다')
#     else:
#         raise ValueError('입력을 확인하세요')
    
# while True:
#     try:
#         ans = input('예/아니오 중 하나를 입력하세요 :')
#         get_ans(ans)
#         break
#     except Exception as e:
#         print('error : ',e)

# fname = input('입력할 파일의 이름 :')
# f = open(fname,'r')

# n = 1
# l = f.readline()

# while l:
#     print('{:3d}: {}'.format(n,l),end='')
#     n+=1
#     l = f.readline()

# f.close()