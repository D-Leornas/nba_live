from nba_live.getgamedata import GetGameData
from nba_live.getboxscore import GetBoxScore
import time
from datetime import datetime, timezone, UTC
import pandas as pd

def dataStream(queue, game_data):    

    activator = {}
    ids = game_data.getGameIds()
    for index, val in enumerate(game_data.getGameTimes()):
        activator[val] = ids[index]
    active_ids = []

    while True:

        key_removal = []

        for game_time in activator.keys():
            if datetime.now(UTC).replace(microsecond=0).replace(tzinfo=None) >= datetime.strptime(game_time, "%Y-%m-%dT%H:%M:%SZ"):
                active_ids.append(activator[game_time])
                key_removal.append(game_time)
            else:
                print(activator[game_time] + " has not started")

        for key in key_removal:
            activator.pop(key)
             
        data_holder = []
        for id in active_ids:
            try:
                boxscore = GetBoxScore(id)
                data_holder.append(boxscore.getBoxScoreData())
            except:
                data_holder.append({
                    "gameId": id,
                    "homeTeamId": None,
                    "awayTeamId": None,
                    "homeTeamPlayers": None,
                    "awayTeamPlayers": None
                })
        
        if len(data_holder) > 0:
            while not queue.empty():
                queue.get()
            queue.put(pd.DataFrame(data=data_holder))

        time.sleep(10)