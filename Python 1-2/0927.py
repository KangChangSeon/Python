#Task 1
def add_numbers(a: float, b: float) -> float:
    # 두 숫자 a 와 b를 더한 결과를 반환
    return a + b
print(add_numbers(10,5))
#Expected output : 15

#Task 2
def calculate_average(numbers: list) -> float:
    # 정수 리스트 numbers의 평균을 계산하여 반환
    res = 0
    for i in numbers:
        res += i
    res /= len(numbers)
    return res
print(calculate_average([4,5,6]))
#Expected output : 5.0

#Task 3
def linear_time_complexity(n: int) -> None:
    # 입력 크기 n에 비례하는 반복을 수행
    for i in range(n):
        print(i) # 어떤 작업을 수행하는 것으로 가정
linear_time_complexity(5)



# #Task 4
def quadratic_time_complexity(n: int) -> None:
    # 이중 반복문을 사용하여 입력 크기 n에 비례하는 작업을 수행
    for i in range(n):
        for j in range(n):
            print(i, j) # 어떤 작업을 수행하는 것으로 가정
quadratic_time_complexity(3)

#Task 5
def calc(n: int) -> int:
    sum = n*(n+1) / 2
    return sum
    # 어떤 수를 입력해도 단 1번 연산하기 때문에 총 연산의 수는 동일하다.
print(calc(5))

def cal_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum

def calc_sum2(n):
    sum = n * (n+1) / 2
    return sum