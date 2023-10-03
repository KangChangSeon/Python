# # 팩토리얼 계산 문제
# def calculate_factorial(n:int) -> int:
#     if n == 0 : return 1 # 0! = 1
#     elif n == 1 : return 1 # 1! = 1
#     else :  return n * calculate_factorial(n-1) # n 과  n 이전의 값들을 모두 곱하여 반환함.

# print(calculate_factorial(5)) #Expected output = 120

# # 문자열 뒤집기 문제
# def reverse_string(input_string:str) -> str:
#     res = "" # 결과값을 저장할 변수
#     for i in range(len(input_string)): # input_string 의 길이만큼 반복
#         res += (input_string[len(input_string)-1-i]) # input_string 의 뒤에서부터 res 에 추가
#     return res

# print(reverse_string("가나다")) #Expected output = "다나가"


# def contains(bag, e):
#     return e in bag

# def insert(bag, e):
#     bag.append(e)

# def remove(bag, e):
#     bag.remove(e)

# def count(bag: list, e: any) -> int:
#     return bag.count(e)

# b = ["휴대폰", "지갑", "손수건", "빗", "자료구조", "야구공"]
# print(f"내 가방 속의 물건: {b}")
# remove(b, "손수건") # 내 가방: b 에서 "손수건" 제거
# insert(b, "빗") # 내 가방: b 에 "빗" 추가
# print(f"내 가방 속의 물건: {b}")
# print(f"빗의 개수 {count(b, '빗')}") # 내 가방: b 에서 "빗" 의 개수 출력

# print()

# c = ["a", "b", "c", "d", "e", "f"]
# print(f"내 차 안의 물건: {c}")
# remove(c, "b") # 내 차: c 에서 "b" 제거
# insert(c, "a") # 내 차: c 에 "a" 추가
# print(f"내 차 안의 물건: {c}")
# print(f"내 차 안의 물건: {count(c, 'a')}") # 내 차: c 에서 "a" 의 개수 출력


# import time # time 모듈 추가

# start = time.time() # 코드 실행 시작 시간 기록

# for i in range(100000000): # 테스트용으로 실행시간이 오래 걸리는 반복문 작성
#     pass

# end = time.time() # 코드 끝나는 시간 기록
# print(f"실행시간 : {end - start}") # 끝난 시간에서 시작 시간을 빼서 실행 시간을 구함
# #Expected output : 실행시간 : (컴퓨터의 성능에 따라 차이가 있음) 
