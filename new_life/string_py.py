# import this  # python之禅


name = "liao"
string = "Hello %s, welcome to python!"

print(string % name.upper())  # 将名字大写
print(string % name.lower())  # 将名字小写
print(string % name.capitalize())  # 将首字母

print(string, "\r", name)
print(string, "\n", name)
