import src
from src.nba_live_D_Leornas.nbalive import NBALive
from multiprocessing import freeze_support
import time

if __name__ == '__main__':
    freeze_support()
    test = NBALive()
    test.start()
    time.sleep(1)

    while True:
        print(test.getPlayerStats("1111111"))
        time.sleep(10)