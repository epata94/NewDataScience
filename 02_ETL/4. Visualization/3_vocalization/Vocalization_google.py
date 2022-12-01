from gtts import gTTS

# default_str="""안녕하세요. 홍길동입니다. 스마트홈네트워크를 구동시키겠습니다.
# 오늘의 뉴스를 알려드리겠습니다.
# 빅데이터 기술 교육이 거의 마무리가 되어가고 있으며
# 이제 졸업작품을 위한 기획단계가 들어가면서
# 학생들의 자율성을 극대화하기 위한 수업으로 진행이 될 예정입니다.
#  안녕!"""
default_str="안녕하세요. 안녕하세요? 안녕하세요! 안녕하세요.. 젠장. 젠장? 젠장!"

def speaker(a):
    tts = gTTS(text=a, lang='ko')
    tts.save("test.mp3")

    open("test.mp3")


speaker(default_str)
# speaker(emotion_str)
