# import datetime

# datetime.datetime.now
# print(datetime.datetime.now())

# today = datetime.date.today()



# print(today)

# print(today.year)
# print(today.month)
# print(today.day)



# start_time = datetime.datetime.now()

# start_time.replace(month=12, day=25)

# print(start_time.replace(month=12, day=25))



# import datetime as dt

# start_time = dt.datetime.now()

# print(start_time.replace(month=12, day=25))



# from datetime import datetime
# start_time = datetime.now()

# print(start_time)



# import datetime as dt

# today = dt.datetime.now()
# print('오늘의 날짜 : {}년 {}월 {}일'.format(today.year,today.month,today.day))

# if today.hour < 12:
#     p = '오전'
#     p_hour = today.hour
# else:
#     p = '오후'
#     p_hour = today.hour - 12
# print('현재시간 : {} {}시 {}분 {}초'.format(p,p_hour,today.minute,today.second))



# import datetime as dt

# today = dt.date.today()
# print('오늘은 {}년 {}월 {}일'.format(today.year,today.month,today.day))

# xMas = dt.datetime(2023, 12, 25)
# time_gap = xMas - dt.datetime.now()

# print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format(\
#     time_gap.days, time_gap.seconds // 3600))



# import datetime as dt

# today = dt.datetime.now()
# hundred = dt.timedelta(days=100)
# plus100day = today + hundred

# print(today)
# print(hundred)
# print(plus100day)


# import datetime as dt
# y,m,d = map(int,input('처음으로 사귄 연도와 월, 일을 입력하시오 :').split())


# day = dt.datetime.now()
# change_d = day.replace(year=y,month=m,day=d)
# print(change_d)

# hun = dt.timedelta(days=100)
# plus100day = change_d + hun

# print(plus100day)



# import time as t

# unix = t.time()
# local_t = t.localtime(unix)
# print(t.strftime('%Y-%m-%d %H-%M-%S',local_t))



# import time

# print('바로 출력되는 문구')
# time.sleep(4.5)
# print('4.5초 후에 출력되는 구문')



# import time as t
# st = t.time()
# print(1+2+3+4+5+6+7+8+9+10)

# et =t.time()
# gap = et - st
# print("1에서 10까지의 합을 구하고 출력하는 시간 : {:7.4f}초".format(gap))



# import math as m
# print(m.pow(3,3)) #제곱
# print(m.fabs(-99)) #실수 절대값
# print(m.ceil(2.1)) #올림값
# print(m.ceil(-2.1)) #올림값
# print(m.floor(2.1)) #내림값
# print(m.log(2.71828))
# print(m.log(100,10)) #로그 10을 밑으로 하는 100값



# import math as m

# print(m.sin(0.0))
# print(m.sin(90.0))
# print(m.sin(3.14159/2.0))

# print(m.pi)
# print(m.sin(m.pi/2.0))



# import math as m

# print(m.radians(90))
# print(m.asin(1.0))
# print(m.degrees(m.asin(1.0)))
# print(m.degrees(m.pi/2.0))
# print(m.tan(2*m.pi))



# #LAB 7-3 405p
# import math as m

# for i in range(0,181,10):
#     print('{:4d} degree ={:6.3f} radian'.format(i,m.radians(i)))



# import random as rd

# print(rd.random()) # 0 이상 1 미만의 실수를 반환함
# print(rd.random()) # 매번 다른 실수를 반환함
# print(rd.randrange(1, 7)) # 1이상 7 미만의 정수를 반환함
# print(rd.randrange(0, 10, 2)) # 1이상 10 미만 정수 중 2의 배수를 반환함
# print(rd.randint(1, 10)) # 1이상 10 이하의 임의의 정수를 반환함



# import random as rd

# numlist = [10,20,30,40,50]
# rd.shuffle(numlist)

# print(numlist)
# print(rd.choice(numlist))
# print(rd.sample(numlist,3))



# import random as rd
# a = list(range(1,11))

# rd.shuffle(a)
# print(a)



#LAB 7-5 408p

# #1
# import random as rd

# a = list(range(0,101,5))

# print(rd.sample(a, 3))

# #2
# b = list(range(1,11))
# print(rd.sample(b,3))