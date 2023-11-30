"""
scaping data from uderstat.com
credits to: https://www.sergilehkyi.com/2019/06/web-scraping-advanced-football-statistics/
"""
from bs4 import BeautifulSoup, element
import requests
import enum
import re
from dataclasses import dataclass, field


class ErrorCodeEnum(enum.Enum):
    OK: 200
    NOT_FOUND: 404


test_url = 'https://understat.com/match/23169'

match_url = 'https://understat.com/match/'
bl_url = 'https://understat.com/league/Bundesliga'

bl23 = 'Bundesliga2023'


@dataclass
class Match:
    id: int = 0
    league: str = ""
    date: str = ""
    team_home: str = ""
    team_away: str = ""
    chances: [int, int] = field(default_factory=list)  # home, away + 100 - sum(home, away)
    goals: [int, int] = field(default_factory=list)  # home, away
    xG: [float, float] = field(default_factory=list)
    shots: [int, int] = field(default_factory=list)
    shots_on_target: [int, int] = field(default_factory=list)
    deep: [int, int] = field(default_factory=list)
    ppda: [float, float] = field(default_factory=list)
    xPTS: [float, float] = field(default_factory=list)


def find_bundesliga_url():
    total_matches = 0
    for i in range(50000):
        req = requests.get(match_url + str(i))
        if req.status_code == ErrorCodeEnum.NOT_FOUND.value:
            print(f'matchcode: {i} does not exist')
            break
        elif req.status_code != ErrorCodeEnum.OK.value:
            print(f'Error code {req.status_code} for matchcode {i}')
            break

        soup = BeautifulSoup(req.text, 'lxml')
        league_year, date = find_league_year_and_date(soup)
        if league_year != bl23:
            break
        print('found a match')
        total_matches += 1

    # 1. iterate every number in url
    # 2. store each match with: teams, date, url
    # 3. sort game to league, week/matchday
    # 4. clearify missing games
    # 5. return dict of urls for every matchday
    return


def find_match_stats(match: Match, soup: BeautifulSoup):
    progress_bars = soup.find_all("div", class_='progress-bar')

    # team names
    team_divs = progress_bars[0].find_all_next("div", class_='progress-value')
    home_team = filter_html_tag_value(team_divs[0])
    away_team = filter_html_tag_value(team_divs[1])
    print(f"match {home_team} against {away_team}")
    match.team_home = home_team
    match.team_away = away_team

    # chances
    iterator = re.findall('title=".*"', str(progress_bars[1]))
    chances_array = []
    for group in iterator:
        regex_group = re.search('".*"', group)
        chances_array.append(regex_group.group()[1:-2])
    print(f"chances separation per team: {chances_array}")
    match.chances = chances_array

    # goals
    regex_goals = re.findall("[0-9]+", progress_bars[2].getText())
    print(f"match score: {regex_goals[0]} : {regex_goals[1]}")
    match.goals = regex_goals


    # xG
    xG_progress_bar = progress_bars[3]
    xG_home_div = xG_progress_bar.find_next('div', class_='progress-home')
    xG_home_value = xG_home_div.find_next('div', class_='progress-value')
    xG_away_div = xG_progress_bar.find_next('div', class_='progress-away progress-over')
    xG_away_value = xG_away_div.find_next('div', class_='progress-value')
    xG_stats = [float(xG_home_value.text), float(xG_away_value.text)]
    print(f"expected goals: {xG_stats[0]} : {xG_stats[1]}")
    match.xG = xG_stats

    # shots
    regex_shots = re.findall("[0-9]+", progress_bars[4].getText())
    print(f"shots per team: {regex_shots[0]} : {regex_shots[1]}")
    match.shots = regex_shots

    # shots on target
    regex_shots_target = re.findall("[0-9]+", progress_bars[5].getText())
    print(f"shots on target per team: {regex_shots_target[0]} : {regex_shots_target[1]}")
    match.shots_on_target = regex_shots_target

    # deep
    regex_deep = re.findall("[0-9]+", progress_bars[6].getText())
    print(f"shots on target per team: {regex_deep[0]} : {regex_deep[1]}")
    match.deep = regex_deep

    # ppda
    ppda = re.findall("[0-9]+.[0-9]+", progress_bars[7].getText())
    print(f"ppda per team: {ppda[0]} : {ppda[1]}")
    match.ppda = ppda

    # xpts
    xpts = re.findall("[0-9]+.[0-9]+", progress_bars[8].getText())
    print(f"xpts per team: {xpts[0]} : {xpts[1]}")
    match.xPTS = xpts

    return



def find_league_year_and_date(soup: BeautifulSoup):
    navigation_line = soup.find_all("ul", class_='breadcrumb')
    if len(navigation_line) != 1:
        print('Parsing error navigation line!')
        return
    links = navigation_line[0].find_all_next('li')

    league_year_regex = re.search('".*"', str(links[1]))
    league_year = league_year_regex.group()[1:-1].removeprefix('league/').replace("/", "")

    date_regex = re.search('>.*<', str(links[2])).group()
    date = date_regex[1:-1]

    return league_year, date


def filter_html_tag_value(html_text: element.PageElement) -> str:
    regex = re.search('>.*<', str(html_text))
    if len(regex.group()) != 0:
        return regex.group()[1:-1]



def main():
    page = requests.get(test_url)
    soup = BeautifulSoup(page.text, 'lxml')
    league_year, date = find_league_year_and_date(soup)
    test_match = Match(23169, league_year, date)
    find_match_stats(test_match, soup)
    print('**********************************')
    print(test_match)


if __name__ =="__main__":
    main()
