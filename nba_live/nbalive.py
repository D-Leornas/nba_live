from nba_live.getgamedata import GetGameData
from nba_live.getboxscore import GetBoxScore
from nba_live.datastream import dataStream
from multiprocessing import Process, Queue
import pandas as pd
import time

class NBALive():
    def __init__(self):
        self.game_data = GetGameData()
        self.last_message = None
        self.queue = Queue()
        self.get_stats_process = Process(target=dataStream, args=(self.queue, self.game_data))

    def start(self):
        self.get_stats_process.start()
        time.sleep(2)

    def stop(self):
        self.get_stats_process.join()

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
    
if __name__ == '__main__':
    pass