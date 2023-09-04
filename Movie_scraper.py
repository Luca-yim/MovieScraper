from bs4 import BeautifulSoup
import requests
import re

html_text = requests.get('https://editorial.rottentomatoes.com/guide/movies-100-percent-score-rotten-tomatoes/').text
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.find_all('div', class_ = 'row countdown-item')

year = input("Enter the year you want to search: ")

for movie in movies:
    movie_title = movie.find('div', class_ = 'article_movie_title')
    date_of_release = movie_title.find('span', class_ = 'subtle start-year').text
    if date_of_release.startswith(year, 1):
        movie_name = movie_title.find('a', attrs={'href': re.compile("^https://www.rottentomatoes.com/m/")}).text
        critique = movie.find('div', class_ = 'info critics-consensus').text.replace('Critics Consensus: ', '')
        movie_director = movie.find('div', class_ = 'info director').text.replace('Directed By: ', '')
        dir = movie_director.replace('\n', '')
        print(f'''
             Movie Title: {movie_name}
             Year: {date_of_release}
             Directed By: {dir}
             Critique: {critique}
             ''')

        print('')
        


