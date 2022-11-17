try:
    ftest=open('D:/Pywork/DataScience/pythonBasic/Chapter8/Test/test.txt',mode='w')
    ftest.write('Life if too short')  # 파일쓰기

    ftest=open('D:/Pywork/DataScience/pythonBasic/Chapter8/Test/test.txt')
    print(ftest.read()) #파일 전체읽기


except Exception as e:
    print(f"ERROR 발생:{e}")
finally:
    ftest.close()