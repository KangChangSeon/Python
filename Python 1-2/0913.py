# arr = [2,17,4,9]
# is_prime=[]

# for n in range(len(arr)):
#     num = arr[n]

#     if num == 1:
#         is_prime = True
#     if num == 2:
#         is_prime = True

#     for i in range(2,num):
#         result = num % i
#         if result == 0:
#             is_prime = False
#             break
#         else:
#             is_prime = True
#             break
#     if is_prime == False:
#         print('{}는 소수가 아닙니다.'.format(num))
#     else:
#         print('{}는 소수입니다.'.format(num))


def fibo(n):
    print(n)

    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))

print(fibo(4))