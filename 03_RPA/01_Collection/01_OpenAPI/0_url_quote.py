import urllib
from urllib.parse import quote_plus
from urllib.parse import unquote_plus

print("<한글 URL 주소>")
url_provided = 'https://example.com/한글메뉴?한글파라메터=한글값'
print(url_provided)

url_encoded = quote_plus(url_provided)

print("\n<인코딩한 한글 URL 주소>")
print(url_encoded)

url_decoded = unquote_plus(url_encoded)
print("\n<디코딩한 한글 URL 주소>")
print(url_decoded)

if url_decoded == url_provided:
    print("\n잘되네요")