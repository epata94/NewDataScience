#7. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라
def make_url(str):
    return f'www.{str}.com'

str = input('문자열을 입력해주세요 : ')

print(make_url(str))



