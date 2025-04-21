str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

_, str = str.split('?')

lst = str.split('&')

dict = {k:v for k, v in (items.split('=') for items in lst)}
print(dict)