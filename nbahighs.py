import time
import datetime
import requests
import tweepy
import pandas as pd

CONSUMER_KEY='XXXXX'
CONSUMER_SECRET='XXXXX'
ACCESS_KEY='XXXXX'
ACCESS_SECRET='XXXXX'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitter = tweepy.API(auth)

useragent = {'user-agent':'chrome'}
gamedate = ""
gamesFinished = []
todaysGames = -1
teamDict = {}
scoresurl = "http://data.nba.com/data/5s/v2015/json/mobile_teams/nba/2017/scores/00_todays_scores.json"
desiredStats = ["PTS", "REB", "AST", "STL", "BLK", "FG3M"]

def team_tweet(teamID):
    if teamID not in teamDict:
        teamurl = "http://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2017-18&TeamID=" + str(teamID)

        r = requests.get(teamurl, headers=useragent)
        r.raise_for_status()
        rows = r.json()['resultSets'][0]['rowSet']
        cols = r.json()['resultSets'][0]['headers']

        df = pd.DataFrame.from_records(rows, columns=cols)
        teamDict[teamID] = df

    for row in teamDict[teamID].itertuples():      
        rv = season_highs(getattr(row, 'PLAYER_ID'))
        if rv != -1:
            post = getattr(row, 'PLAYER') + " put up a season high " + rv
            try:
                twitter.update_status(post)
                print('[{}]'.format(datetime.datetime.now()), post)
            except tweepy.TweepError as e:
                if e.response.text[19:22] == '187':
                    print('[{}]'.format(datetime.datetime.now()), 'Handling duplicate tweet')
                    pass
                else:
                    raise e
        

def season_highs(playerID):
    playerurl = "http://stats.nba.com/stats/playerprofilev2?LeagueID=00&PerMode=PerGame&PlayerID=" + str(playerID)
    r = requests.get(playerurl, headers=useragent)
    r.raise_for_status()

    rows = r.json()['resultSets'][12]['rowSet']
    cols = r.json()['resultSets'][12]['headers']
    df = pd.DataFrame.from_records(rows, columns=cols)
    df = df[df['GAME_DATE'] == gamedate]
    df = df[df['STAT'].isin(desiredStats)]
    
    if len(df) > 0:
        highs = []
        for row in df.itertuples():
            highs.append(str(getattr(row, 'STAT_VALUE')) + ' ' + getattr(row, 'STAT'))
        tweet = ', '.join(highs) + " against " + df['VS_TEAM_ABBREVIATION'][0] + " today. #NBAStats"
        return tweet
    return -1

def main():
    r = requests.get(scoresurl, headers=useragent)
    r.raise_for_status()

    global gamedate, todaysGames, gamesFinished
    gamedate = time.strftime("%b %d %Y", time.strptime(r.json()['gs']['gdte'], "%Y-%m-%d")).upper()
    games = r.json()['gs']['g']
    todaysGames = len(games)
    for g in games:
        if g['stt'] == 'Final' and g['gid'] not in gamesFinished:
            team_tweet(g['h']['tid'])
            team_tweet(g['v']['tid'])
            gamesFinished.append(g['gid'])
        elif g['gid'] in gamesFinished:
            print('[{}]'.format(datetime.datetime.now()), g['gcode'], "completed")
        else:
            print('[{}]'.format(datetime.datetime.now()), g['gcode'], "has not ended")


while todaysGames != len(gamesFinished):
    main()
print('[{}]'.format(datetime.datetime.now()), "Finished today's games!")