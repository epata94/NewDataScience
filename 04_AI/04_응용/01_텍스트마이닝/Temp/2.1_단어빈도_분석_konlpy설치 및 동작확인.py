#py -m pip install JPype1-0.6.3-cp36-cp36m-win_amd64.whl
#py -m pip install konlpy

from konlpy.tag import Okt
okt = Okt()
malist = okt.pos("아버지가 방에 들어가신다.", norm=True, stem=True)
# malist = okt.pos("아버지 가방에 들어가신다.", norm=True, stem=True)
print(malist)
