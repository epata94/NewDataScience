import urllib.request
client_id = "CJsADWzyJq8m29Qm7l11"           # <= 변경
client_secret = "cv55RE05hD" # <= 변경
default_str="""안녕하세요. 홍길동입니다. 스마트홈네트워크를 구동시키겠습니다. 
오늘의 뉴스를 알려드리겠습니다.
빅데이터 기술 교육이 거의 마무리가 되어가고 있으며 
이제 졸업작품을 위한 기획단계가 들어가면서 
학생들의 자율성을 극대화하기 위한 수업으로 진행이 될 예정입니다.
 안녕!"""
emotion_str="안녕하세요. 안녕하세요? 안녕하세요! 안녕하세요.. 젠장. 젠장? 젠장!"
# encText = urllib.parse.quote(emotion_str)
encText = urllib.parse.quote(default_str)
data = "speaker=jinho&speed=0&text=" + encText;
url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('11112.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)