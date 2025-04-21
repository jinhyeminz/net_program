data = input("")
data = data.split()
a = int(data[0])
b = int(data[2])
if a >= b:
    if data[1] == '+':
        result = a + b
            
    elif data[1] == '-':
        result = a - b

    elif data[1] == '*':
        result = a * b

    elif data[1] == '/':
        result = round(a / b, 1)            
            
else:
    if data[1] == '+':
        result = a + b
            
    elif data[1] == '-':
        result = b - a

    elif data[1] == '*':
        result = a * b

    elif data[1] == '/':
        result = round(b / a, 1)


result = str(result)
print(result)
print(type(result))