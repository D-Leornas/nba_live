from nba_api.live.nba.endpoints import scoreboard
import pandas as pd

class GetGameData:
    def __init__(self):

        sb = scoreboard.ScoreBoard()
        sb = sb.get_dict()
        sb_pd = pd.DataFrame.from_dict(sb)

        data_holder = []

        for game in sb_pd.scoreboard.games:
            data_holder.append([
                    game["gameId"],
                    game["gameTimeUTC"],
                    pd.DataFrame(data={
                        "teamId": [game["homeTeam"]["teamId"]],
                        "teamName": [game["homeTeam"]["teamName"]]
                    }),
                    pd.DataFrame(data={
                        "teamId": [game["awayTeam"]["teamId"]],
                        "teamName": [game["awayTeam"]["teamName"]]
                    })
            ]
            )

        self.return_dataframe = pd.DataFrame(data_holder, columns=['gameId', 'gameTimeUTC', 'homeTeam', 'awayTeam'])
    
    def getDataFrame(self):
        return self.return_dataframe
    
    def getGameIds(self):
        return [id for id in self.return_dataframe['gameId']]

    def getGameTimes(self):
        return [time for time in self.return_dataframe['gameTimeUTC']]