''''
celeb crop image split(celeb_crop_5)
 1. image read
 2. x_val(50) vs x_train(51~end) split
 3. label : 0 ~ 4(celeb5)
 4. data set save(data 폴더 생성)
'''
'''
 특정 디렉터리에서 *.png 파일만 디렉터리에 이동하기
 1. os.path.exists(path) : 디렉터리 유무 확인 
 2. glob(path/*.png) : png 검색
 3. png 이진 파일 읽기 
 4. png 이진 파일 쓰기 & 디렉터리 이동 
'''
import os # dir or file path
from glob import glob # *, ? 파일 검색

# (1) image 파일 경로
print(os.getcwd()) # D:\Pywork\workspace
img_path = 'chapter08/images/' # 이미지 원본 디렉터리
img_path2 = 'chapter08/images2/' # 이미지 이동 디렉터리

# (2) 디렉터리 존재 유무
if os.path.exists(img_path) :
    print('해당 디렉터리가 존재함')

    # (3) image 파일 저장, 파일 이동 디렉터리 생성
    images = [] # png 파일 저장
    os.mkdir(img_path2) # 파일 이동 디렉터리 생성

    # (4) images 디렉터리에서 png 검색
    for pic_path in glob(img_path + '*.png'): # images 디렉터리에서 png 검색
        # (5) 경로와 파일명 분리, 파일명 추가
        img_path = os.path.split(pic_path) # ('chapter08/images', '101.png')
        images.append(img_path[1]) # png 파일명 추가

        # (5) 이진파일 읽기
        rfile = open(file=pic_path, mode='rb')
        output = rfile.read()

        # (6) 이진파일 쓰기 -> chapter08/png 폴더 이동
        wfile = open(img_path2+img_path[1], mode='wb')
        wfile.write(output)

    rfile.close(); wfile.close()
else:
    print('해당 디렉터리가 없음')

print('png file =', images)
# png file = ['101.png', '102.png', '103.png', '104.png', '105.png']

