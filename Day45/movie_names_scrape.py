from bs4 import BeautifulSoup as bs
import requests

# get the data
response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
soup = bs(response.text, 'lxml')

# save the name of movies in a list
names = [i.text for i in soup.select('h3.title')]
names.reverse()

# store the name of movies in a .txt file
with open('movies_to_watch.txt', mode='w', encoding='utf-8') as f:
    for name in names:
        f.write(name+'\n')