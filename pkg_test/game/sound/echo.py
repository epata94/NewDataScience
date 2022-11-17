def echo_test():
    print("echo")

# 메인 컨트롤러 프로그램과 별개로 독립적으로 개발 함수를 테스트하고
# 싶을때 __name__ 시작점을 개별 모듈에 지정할 수 있다.
# 따라서 컨트롤러 수행시 아래 코드는 수행되지 않고 개별모듈에서
# 수행할 경우에만 독립적으로 수행된다.
if __name__ == "__main__":
    echo_test()