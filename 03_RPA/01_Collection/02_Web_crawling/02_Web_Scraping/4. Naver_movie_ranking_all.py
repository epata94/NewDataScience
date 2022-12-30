from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

ranks = soup.findAll('img', attrs={'width':'14'})
tags = soup.findAll('div', attrs={'class':'tit3'})
up_downs =  soup.findAll('img', attrs={'class':'arrow'}) 
ranges = soup.findAll('td', attrs={'class':'range ac'})

f = open('movie_rank_test.csv', 'w', encoding='utf-8')
# f = open('movie_rank_test.csv', 'w', encoding='cp949')
f.write('rank, title, µî¶ôÆø, updown\n')
i = 0
while i < len(ranks)-1:
    print('{0}, {1}, {2}, {3}'.format(int(ranks[i]['alt']), tags[i].a['title'], ranges[i].string, up_downs[i]['alt']))
    f.write('{0}, {1}, {2}, {3}\n'.format(int(ranks[i]['alt']), tags[i].a['title'], ranges[i].string, up_downs[i]['alt']))
    i += 1
f.close()