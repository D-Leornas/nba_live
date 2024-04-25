from nba_live.getgamedata import GetGameData
from nba_live.getboxscore import GetBoxScore
import time
from datetime import datetime, timezone
import pandas as pd

def dataStream(queue, game_data):    

    activator = {}
    ids = game_data.getGameIds()
    for index, val in enumerate(game_data.getGameTimes()):
        activator[val] = ids[index]
    active_ids = []

    while True:
        
        for game_time in activator.keys():
            if datetime.now().replace(tzinfo=timezone.utc).timestamp() >= datetime.strptime(game_time, "%Y-%m-%dT%H:%M:%SZ").timestamp():
                active_ids.append(activator[game_time])
                activator.pop(game_time)
            else:
                print(activator[game_time] + " has not started")
             
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