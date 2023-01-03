import struct
def to_csv(name, maxdata):
    # 레이블 파일과 이미지 파일 열기
    lbl_f = open("./mnist/"+name+"-labels-idx1-ubyte", "rb")
    img_f = open("./mnist/"+name+"-images-idx3-ubyte", "rb")
    csv_f = open("./mnist/"+name+".csv", "w", encoding="utf-8")
    # 헤더 정보 읽기 --- (※1)
    # >|| big-endian 방식으로 데이터 조회
    # >|| <== 데이터를 읽을 때 big-endian 방식으로 읽을 경우
    # (데이터를 표현 할 때 주소가 큰 값부터 적용함, 대표적인 프로세서: PowerPC, Sun)
    # <|| <== little-endian (데이터를 표현할 때 주소를 작은 값부터 활용한다.)
    # 대표적인 little-endian 프로세서: Intel
    # read() <= 특정 바이트 많큼 데이터를 읽어오는 함수

    # 메타 정보를 읽어 오는 코드
    # 메타 정보: 실제 데이터에 대한 정보를 기술 하는 부가 정보
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag, img_count = struct.unpack(">II", img_f.read(8))
    # rows: 28, cols: 28
    rows, cols = struct.unpack(">II", img_f.read(8))
    # pixels : 784
    pixels = rows * cols
    # 이미지 데이터를 읽고 CSV로 저장하기 --- (※2)
    res = []

    # lbl_count: 60000
    # 실제 데이터를 읽어 오는 코드
    for idx in range(lbl_count):
        if idx > maxdata: break
        # "B" 숫자를 unsigned char 형식으로 읽기 위한 옵션
        # label은 1byte씩 저장하고 있기 때문에
        label = struct.unpack("B", lbl_f.read(1))[0]
        # label에 해당 되는 이미지는 28*28 pixel이기 때문에 784 byte를 통째로 읽는다.
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label)+",")
        csv_f.write(",".join(sdata)+"\r\n")
        # 잘 저장됐는지 이미지 파일로 저장해서 테스트하기 -- (※3)
        if idx < 10:
            s = "P2 28 28 255\n" # <= 실제 pgm 파일의 메타정보
            s += " ".join(sdata)
            iname = "./mnist/{0}-{1}-{2}.pgm".format(name,idx,label)
            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)
    csv_f.close()
    lbl_f.close()
    img_f.close()
# 결과를 파일로 출력하기 --- (※4)
# 처음에 1000, 500으로 데이터를 생성후 머신러닝 결과를 본 후 그 다음에 모든 데이터를 활용할 것
to_csv("train", 1000)
to_csv("t10k", 500)
# to_csv("train", 60000)
# to_csv("t10k", 10000)
