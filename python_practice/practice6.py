# d = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
#     {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
#     {'name':'Princess', 'phone':'555-3141', 'email':''},
#     {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

# # 전화번호가 8로 끝나는 사용자 이름을 출력하라.
# for i in d:
#     if i['phone'][-1] == '8':
#         print(i['name'])
# print('\n')

# # 이메일이 없는 사용자 이름을 출력하라.
# for j in d:
#     if j['email'] == '':
#         print(j['name'])
#     else:
#         pass

# # 사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라.
# name_input = input('사용자 이름을 입력하세요: ')
# for k in d:
#     if name_input in k['name']:
#         print('phone:{}, email:{}'.format(k['phone'], k['email']))
#         break
#     else:
#         print('이름이 없습니다.')




str = 'led=on&motor=off&switch=off'
list = str.split('&')

# dict = {k: v for k, v in (lst.split('=') for lst in list)}
# 위 코드와 아래 코드는 같은 동작을 하는 코드임
# dict = {}
# for lst in list:
#     k, v = lst.split('=')
#     dict[k] = v

print(dict)