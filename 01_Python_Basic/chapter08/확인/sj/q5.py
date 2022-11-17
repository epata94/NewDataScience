def show_candidates(candidate_list):
    for candidate in candidate_list :
        print(candidate)

def make_idol(candidate_list) :
   for candidate in candidate_list :
       print(f'신예 아이돌 {candidate} 인기 급상승')


def make_world_star(candidate_list) :
    for candidate in candidate_list :
        print(f'아이돌 {candidate} 월드스타 등극')

try:
    file = open("연습생.txt", mode = 'r', encoding='utf-8')
    candidate_list = file.read().split()
except Exception as e:
    print('Error 발생 : ', e)
finally:
    file.close()

show_candidates(candidate_list)
make_idol(candidate_list)
make_world_star(candidate_list)

