import pytest
from nba_live.nbalive import NBALive

@pytest.fixture
def test():
    return NBALive()
