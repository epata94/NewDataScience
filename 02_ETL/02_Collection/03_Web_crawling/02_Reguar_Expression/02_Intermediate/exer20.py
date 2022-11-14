import re
pat = re.compile(".*[@].*[.](?=com|net$).*$")

print(pat.match('paere@gmail.com'))
print(pat.match('dkfdf@daum.net'))
print(pat.match('dfkse@hmyome.co.kr'))
