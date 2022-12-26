import re
original_text="""a1 dkfjsjkflsdjflsdjflsdfkj
b3 dkfjskdlfjslfjlsjfl
3k dkjflskdjfklsdjkfl
5j djkfjsklfjsljfsjdfljsdlf
k4 dkjfkdjfldsfjllfs
9p djkfdjsf
u9 djkfjksdjfsljfdslfjl
"""
p=re.compile('[a-zA-Z0-9][0-9]')
m = p.match(original_text)
print(m)