# 3-1번
# from random import randint
# dollar = 50
# while True:
#     if not dollar <= 0 or dollar == 100:
#         coin = randint(1, 2)
#         answer = int(input('앞면(1) 또는 뒷면(2)을 입력하세요.: '))
#         if answer == coin:
#             dollar += 9
#         else:
#             dollar -= 10
#         print(dollar)
#     else:
#         break

# 3-2번 문제
def gcd(a, b):
    if a > b:
        num1 = a
        num2 = b
    else:
        num1 = b
        num2 = a
    
    while not num2 <= 0:
        if num1 > num2:
            q = num1 % num2
            num1 = num2
            num2 = q
        result = num1
    
    print(result)

gcd(12, 24)