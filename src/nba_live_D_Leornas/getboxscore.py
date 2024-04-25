from nba_api.live.nba.endpoints import boxscore
import pandas as pd

class GetBoxScore:
    def __init__(self, id):
        bs = boxscore.BoxScore(id)
        bs = bs.get_dict()
        bs_pd = pd.DataFrame.from_dict(bs)
        home_team_id = bs_pd.game.homeTeam['teamId']
        away_team_id = bs_pd.game.awayTeam['teamId']
        home_data_holder = []
        away_data_holder = []

        for home_player in bs_pd.game.homeTeam['players']:
            home_data_holder.append(home_player)

        for away_player in bs_pd.game.awayTeam['players']:
            away_data_holder.append(away_player)
        
        self.box_score_data = {
            "gameId": id,
            "homeTeamId": home_team_id,
            "awayTeamId": away_team_id,
            "homeTeamPlayers": pd.DataFrame(home_data_holder),
            "awayTeamPlayers": pd.DataFrame(away_data_holder)
        }

    def getBoxScoreData(self):
        return self.box_score_data
