"""
scaping data from uderstat.com
credits to: https://www.sergilehkyi.com/2019/06/web-scraping-advanced-football-statistics/
"""
from bs4 import BeautifulSoup
import requests


test_url = 'https://understat.com/match/23169'


def main():
    page = requests.get(test_url)
    soup = BeautifulSoup(page.text, 'lxml')
    #print(soup)
    progress_bars = soup.find_all("div", class_='progress-bar')
    print(len(progress_bars))
    xG_progress_bar = progress_bars[3]
    xG_home_div = xG_progress_bar.find_next('div', class_='progress-home')
    xG_home_value = xG_home_div.find_next('div', class_='progress-value')
    print(f'Expected Goal home team: {xG_home_value.text}')
    xG_away_div = xG_progress_bar.find_next('div', class_='progress-away progress-over')
    xG_away_value = xG_away_div.find_next('div', class_='progress-value')
    print(f'Expected Goal away team: {xG_away_value.text}')

if __name__ =="__main__":
    main()