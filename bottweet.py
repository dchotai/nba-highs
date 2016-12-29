# Made by Divyesh Chotai 2016
import tweepy
import requests
import time
from pandas import DataFrame
from sortedactiveplayers import players
from botdata import parseSeasonHigh
from datetime import datetime

"""
Checks if any teams are finished playing. If so, check for
season highs of those teams' players and tweet them. Records
teams that have been checked to prevent redundant tweets.
Exits if no games today or no teams have finished playing.
"""

CONSUMER_KEY='XXXXX'
CONSUMER_SECRET='XXXXX'
ACCESS_KEY='XXXXX'
ACCESS_SECRET='XXXXX'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitter = tweepy.API(auth)

def finishedTeams():
    r = requests.get('http://data.nba.com/data/5s/v2015/json/mobile_teams/nba/2016/scores/00_todays_scores.json')
    r.raise_for_status()
    todaysscores = r.json()
    headscores = todaysscores['gs']['g']
    valscores = todaysscores['gs']['g'][0]
    df = DataFrame(headscores, columns = valscores)
    finishedteams = []
    gamecount = df.count()[0]
    for index, row in df.iterrows():
        if row["stt"] == 'Final':
            # Get team IDs of home and visiting teams
            finishedteams += [row['h']['tid'], row['v']['tid']]
    return finishedteams, gamecount

teams, gamecount = finishedTeams()

# Clear seen.txt and exit if no games today or no teams are finished
if gamecount == 0 or teams == []:
    with open('seen.txt', 'w') as f:
        pass
    quit()

# Record teams whose players have already been checked
seen = []
with open('seen.txt', 'r') as f:
    for line in f:
        seen += [int(i) for i in line.split()]

# Tweet season highs of players that finished a game today
for t in teams:
    if t not in seen:
        for p in players[t]:        
            post = parseSeasonHigh(p)
            if post:
               twitter.update_status(post)
               time.sleep(10)

# Add teams whose players have been checked to seen.txt
with open('seen.txt', 'a') as f:
    for t in teams:
        if t not in seen:
            f.write(str(t) + '\n')

