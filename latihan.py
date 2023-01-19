import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
# client = MongoClient('mongodb+srv://feren:feren@cluster0.i3qcsvi.mongodb.net/?retryWrites=true&w=majority')
# db = client.dbsparta

# db.testing.insert_one({'name':'bobby','age':21})

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = 'https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=1BJKFC53QVDD5JY8K29C&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'

data = requests.get(url=url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# movies = soup.select('.lister > table > tbody > tr')

og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

# print(og_image)
# print(og_title)
# print(og_description)


image = og_image['content']
title = og_title['content']
desc = og_description['content']

print(image)
print(title)
print(desc)


# db.movies.drop()

# for movie in movies:
#     movie_title = movie.select_one('.titleColumn > a').text
#     year = movie.select_one('.titleColumn > .secondaryInfo').text
#     year = year.replace('(', '')
#     year = year.replace(')', '')
#     rating = movie.select_one('.ratingColumn > strong').text
#     print(movie_title, '/', year, '/', rating)
    # db.movies.insert_one({'title':movie_title,'year':year, 'rating':rating})
