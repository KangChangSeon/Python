#txt3= "친구가 "햇님이 좋아!"라고 말했다." syntax error
txt3= '친구가 "햇님이 좋아!"라고 말했다.'   #아래처럼 변경하면 사용 가능
txt3= "친구가 \"햇님이 좋아!\"라고 말했다." #\" 백 슬래쉬로 표현 가능
print(txt3)

txt4= 'banana\tapple\torange' #\n 으로 줄바꿈
print(txt4)

txt5 = '''Let's go''' #''' 또는 """ 시작과 끝까지 그대로 출력
print(txt5)

long_str="""사과는 맛있어
맛있는 건 바나나
"""
print(long_str)

print(0.1 + 0.1 == 0.2)

print(0.1 + 0.1 + 0.1 == 0.3)

print(0.1 + 0.1 + 0.1)

print(2**32)

print(14.2 // 5.3)
print(14.2 % 5.3)
print(14.2 - (5.3 * 2))

a=8+2j
b=4+3j
print(a+b)

c1= 2 + 3j
c2 = c1.conjugate
c2 = (2 - 3j)
print(abs(c1))

c3 = c1 * c2
c3 = (13 + 0j)
print(abs(c1) * abs(c1))

print(bin(9))
print(oct(9))
print(hex(9))