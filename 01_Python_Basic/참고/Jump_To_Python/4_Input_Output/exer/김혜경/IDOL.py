def show_candidates(candidate_list):
    for candidate in candidate_list:
        print(candidate, end='')

def make_idol(candidate_list):
    for candidate in candidate_list:
        print("신예 아이돌 %s 인기 급상승"%candidate)
        print("신예 아이돌 %s 인기 급상승".format(...))
        print(f'신예 아이돌 {candidate} 인기급상승')

def make_world_star(candidate_list):
    for candidate in candidate_list:
        print("아이돌 %s 월드스타 등극"%candidate)

f = open("연습생.txt", 'r', encoding='UTF-8')
candidate_list = []
temp_list = f.readlines()
for temp in temp_list:
    candidate_list.append(temp.rstrip())
f.close()

show_candidates(temp_list)
make_idol(candidate_list)
print('')
make_world_star(candidate_list)
