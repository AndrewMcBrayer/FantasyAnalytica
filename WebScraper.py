import requests
scores = {}
for week in range(1, 14):
    r = requests.get('http://games.espn.com/ffl/api/v2/scoreboard',
                     params={'leagueId': 310279, 'seasonId': 2018, 'matchupPeriodId': week})
    scores[week] = r.json()
df =[]
for key in scores:
    temp = scores[key]['scoreboard']['matchups']
    for match in temp:
        df.append([key,
                   match['teams'][0]['team']['teamAbbrev'],
                   match['teams'][1]['team']['teamAbbrev'],
                   match['teams'][0]['score'],
                   match['teams'][1]['score']])

print(df)