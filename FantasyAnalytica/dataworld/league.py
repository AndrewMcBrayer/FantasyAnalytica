import requests
from . import team


"""
Here is an example of the various json requests we are calling into for reference 


Scoreboard Data for a single matchup
====================================================================================
{}Json
    {}LeagueSchedule
        []scheduleitems
            {}0
                []matchups
                    {}0
                        []awayTeamScores
                        {}awayTeam
                            teamId
                            waiver rank    
                            













"""

# setting up some variables
class League(object):
    def __init__(self, id_league, year_current, year_birth):
        self.id_league = id_league
        self.year_current = year_current
        self.year_birth = year_birth

    def _sbData_get(self):
        data_scoreboard_season = {}  # Temp var to collect json data for a particular season
        data_scoreboard = [] #3d array [year][week][data]
        for year in range(self.year_birth, self.year_current):
            for week in range(1, 14):
                r = requests.get('http://games.espn.com/ffl/api/v2/schedule',
                        params={'leagueId': self.id_league, 'seasonId': year, 'matchupPeriodId': week})
                data_scoreboard_season[week] = r.json()
            data_scoreboard.append(data_scoreboard_season)
        self.data_scoreboard =data_scoreboard


    def _sbData_parse_(self):
        # organizes matchups for all three years

        matchups = []  # 3d array --> year,week, homeTeamID, awayTeamID
        scores_league = []  # 3d array --> [year][week][team,score]
        for year in range(0, self.year_current-self.year_birth):
            matchups_season =[]
            scores_league_season = []
            print(self.data_scoreboard[year])
            for key in self.data_scoreboard[year]:
                temp = self.data_scoreboard[year][key]['scoreboard']['matchups']
                temp2 = []
                for match in temp:
                    matchups_season.append([key,
                            match['teams'][0]['teamId'],
                            match['teams'][1]['teamId']])
                    temp2.append(match['teams'][0]['teamId'])
                    temp2.append(match['teams'][0]['score'])
                    temp2.append(match['teams'][1]['teamId'])
                    temp2.append(match['teams'][1]['score'])
                scores_league_season.append(temp2)
            matchups.append(matchups_season)
            scores_league.append(scores_league_season)
        self.matchups = matchups
        self.scores_league = scores_league
        print(scores_league.sort)

    def teams_build(self):
        active = bool(1)
        teams = [team([1], "J Lee", not active), team([2], "Dan", active), team([3], "J Bessex", not active),
                 team([4], "Sahil", active), team([5], "Jimmy", active), team([6], "Shane", active),
                 team([7], "Tyler Brown", not active), team([8], "PK", active), team([9], "Isaac", active),
                 team([10], "Shoey", active), team([11], "WIll", active), team([12], "Andy", active),
                 team([0], "Mike", active), team([0], "Todd", active), team([0], "Mark", active)]