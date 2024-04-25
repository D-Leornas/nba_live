[![Version: PyPI](https://img.shields.io/pypi/v/nba_live.svg?longCache=true&style=for-the-badge&logo=pypi)](https://pypi.python.org/pypi/nba_live)
[![License: MIT](https://img.shields.io/github/license/D-leornas/nba_live.svg?style=for-the-badge)](https://github.com/D-Leornas/nba_live/blob/master/LICENSE)

# nba_live

## An interface for the nba_api boxscore endpoint

This package allows a user to easily grab data from the boxscore endpoint in the nba_api package. This package is still very young, is not tested thoroughly, and is extremely feature depraved.

That being said, if you'd like to install,

## Installation

The live data is stored in dataframes so pandas is required to use this package.

```bash
pip install nba_live
```

## How To Use

```python
    from nba_live.nbalive import NBALive

    if __name__ == '__main__':
        data_stream = NBALive()
        data_stream.start()

        # Call this at any time to get a dataframe of stats for the current day's games
        data_stream.getStats()
```

The data is currently organized in a data frame where each row is organized as follows:

```json
{
  "gameId": "id",
  "hometeamId": "home_team_id",
  "awayTeamId": "away_team_id",
  "homeTeamPlayers": "dataframe holding player data",
  "awayTeamPlayers": "dataframe holding player data"
}
```

The player data is organized as follows:

```json
{
  "status": "ACTIVE",
  "order": 1,
  "personId": 1627759,
  "jerseyNum": "7",
  "position": "SF",
  "starter": "1",
  "oncourt": "0",
  "played": "1",
  "statistics": {
    "assists": 8,
    "blocks": 0,
    "blocksReceived": 0,
    "fieldGoalsAttempted": 12,
    "fieldGoalsMade": 6,
    "fieldGoalsPercentage": 0.5,
    "foulsOffensive": 0,
    "foulsDrawn": 4,
    "foulsPersonal": 1,
    "foulsTechnical": 0,
    "freeThrowsAttempted": 7,
    "freeThrowsMade": 7,
    "freeThrowsPercentage": 1.0,
    "minus": 50.0,
    "minutes": "PT25M01.00S",
    "minutesCalculated": "PT25M",
    "plus": 65.0,
    "plusMinusPoints": 15.0,
    "points": 21,
    "pointsFastBreak": 0,
    "pointsInThePaint": 6,
    "pointsSecondChance": 0,
    "reboundsDefensive": 2,
    "reboundsOffensive": 0,
    "reboundsTotal": 2,
    "steals": 1,
    "threePointersAttempted": 5,
    "threePointersMade": 2,
    "threePointersPercentage": 0.4,
    "turnovers": 2,
    "twoPointersAttempted": 7,
    "twoPointersMade": 4,
    "twoPointersPercentage": 0.5714285714285711
  },
  "name": "Jaylen Brown",
  "nameI": "J. Brown",
  "firstName": "Jaylen",
  "familyName": "Brown"
}
```
