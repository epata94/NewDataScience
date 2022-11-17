# 5.	<연습생 아이돌 만들기>
# '연습생.txt' 파일의 이름을 읽어와 리스트로 만든다.
# def show_candidates(candidate_list): 이라는 함수에서 현재 연습생 리스트를 출력한다.
# def make_idol(candidate_list): 함수에서 이름 앞 뒤로 아래와 같이 문구를 추가하여 메세지를 출력한다.
# 예) 신예 아이돌 유라 인기 급상승
# def make_world_star(candidate_list): 함수에서 이름을 활용해 아래와 같은 문구를 추가하여 메세지를 출력한다.
# 예) 아이돌 유라 월드스타 등극
def show_candidates(candidate_list):
    print(candidate_list)
def make_idol(candidate_list):
    for candidate in candidate_list:
        print(f'신예 아이돌 {candidate} 인기 급상승')

def  make_world_star(candidate_list):
    for candidate in candidate_list:
        print(f'아이돌 {candidate} 월드스타 등극')

try:
    trainee_file = open('D:/Pywork/DataScience/pythonBasic/Chapter8/Test/연습생.txt', encoding="UTF8")
    read_trainee_file=trainee_file.readlines()
    candidate_list=[]
    for name in read_trainee_file:
        candidate_list.append(name.strip())

    show_candidates(candidate_list)
    make_idol(candidate_list)
    make_world_star(candidate_list)
except Exception as e:
    print(f"에러발생: {e}")
finally:
    trainee_file.close()
