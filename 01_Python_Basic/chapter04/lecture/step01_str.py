'''
string 객체 특징
 - 문자들의 모음
 - 일정한 순서를 갖는다.
 - 색인을 이용하여 원소를 참조할 수 있다.
'''

help(str) # Help on class str in module builtins:

# str 클래스 형식
str_var = str(object='string')
print(str_var)
print(type(str_var))
print(str_var[0])
print(str_var[-1])

# str 클래스 간편 형식
str_var2 = 'string'
print(str_var2)
print(type(str_var2))
print(str_var2[0])
print(str_var2[-1])


help(list) # Help on class list in module builtins:
help(tuple) # Help on class tuple in module builtins: