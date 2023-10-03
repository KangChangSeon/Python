# while True:
#     line = input()
#     if line == '#':
#         break

#     # 입력된 문장을 소문자로 변환하여 처리하고, 모음을 카운트합니다.
#     vowel_count = 0
#     for char in line.lower():
#         if char in ['a', 'e', 'i', 'o', 'u']:
#             vowel_count += 1

#     print(vowel_count)


# while True:
#     line = input().split()
#     if line == ['#', '0', '0']:
#         break
    
#     name = line[0]
#     age = int(line[1])
#     weight = int(line[2])
    
#     if age > 17 or weight >= 80:
#         print(name, 'Senior')
#     else:
#         print(name, 'Junior')


n = input().split()
print(type(n))
result = sorted(n)
num1 = int(result[0])
num2 = int(result[1])
num3 = int(result[2])

ok = []
ok.append(num1)
ok.append(num2)
ok.append(num3)

print(ok)