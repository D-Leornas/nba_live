from src.nba_live_D_Leornas.getgamedata import GetGameData
from src.nba_live_D_Leornas.getboxscore import GetBoxScore
from src.nba_live_D_Leornas.datastream import dataStream
from multiprocessing import Process, Queue
import pandas as pd
import time

class NBALive():
    def __init__(self):
        self.game_data = GetGameData()
        self.last_message = pd.DataFrame()
        self.queue = Queue()
        self.get_stats_process = Process(target=dataStream, args=(self.queue, self.game_data))

    def start(self):
        self.get_stats_process.start()

    def getStats(self):
        if not self.queue.empty():
            self.last_message = self.queue.get()
        return self.last_message
    
    def getPlayerStats(self, player_id):
        for index, row in self.last_message.iterrows():
            for player in row.homeTeamPlayers:
                if player.personId == player_id:
                    return player
        return pd.DataFrame()