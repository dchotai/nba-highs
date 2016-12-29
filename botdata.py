# Made by Divyesh Chotai 2016
import requests
from pandas import DataFrame
from datetime import datetime, timedelta

"""
Scrapes API for season highs of player and determines if season
high stat occurred in today's game. If so, returns tweet.
"""

today = datetime.today().date()
today = "{}-{}-{}".format(today.year, today.month, today.day) 

# Header necessary for accessing API without a browser
h = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/55.0.2883.95 Safari/537.36')}

def parseSeasonHigh(player):
    baseurl = 'http://stats.nba.com/stats/playerprofilev2?LeagueID=00&PerMode=PerGame&PlayerID={playerID}'
    r = requests.get(baseurl.format(playerID = player[0]), headers = h)
    r.raise_for_status()
    data = r.json()
    heads = data['resultSets'][12]['headers']
    vals = data['resultSets'][12]['rowSet']
    df = DataFrame(vals, columns = heads)
    # Obtain player name in a FirstName LastName format
    name = [" ".join(n.split(", ")[::-1]) for n in [player[1]]][0]
    rv = name + " put up a season-high "
    allow = False
    opp = ""
    for index, row in df.iterrows():
        # Check if season high > 0, season high occurred today, and stat is of a certain category
        if row[8] > 0 and row[10][:10] == today and row[7] in ["PTS", "REB", "AST", "STL", "BLK", "FG3M"]:
            allow = True
            rv += '{} {}, '.format(row[8], row[7])
            opp = row[6]

    if allow:
        return rv[:-2] + ' against {} today. #NBAStats'.format(opp)