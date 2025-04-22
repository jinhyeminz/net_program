# # 4-1 문제
# word = str(input('Your word: '))
# idx = word.index('a') + 1
# print(word[:idx])
# print(word[idx:])

# # 4-2 문제
# sum = 0
# for i in range(1, 1000):
#     s = str(i)
#     for j in s:
#         sum += int(j)
# print(sum)

# 4-3 문제
lst1 = []
lst2 = []
for i in range(50):
    lst1.append(i)
    lst2.append(i**2)
print(lst1)
print(lst2)