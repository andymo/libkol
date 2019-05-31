from typing import NamedTuple, Dict
from yarl import URL

from .request import Request

import pykollib

from ..Stat import Stat
from ..util import parsing

gym_stat_mapping = {
    Stat.Mysticality: 1,
    1: Stat.Mysticality,
    Stat.Moxie: 2,
    2: Stat.Moxie,
    Stat.Muscle: 3,
    3: Stat.Muscle,
}


class Response(NamedTuple):
    substats: Dict[str, int]
    stats: Dict[str, int]
    level: int


class clan_rumpus_gym(Request):
    def __init__(self, session: "pykollib.Session", stat: Stat, turns: int) -> None:
        """
        Visits the a gym in the clan rumpus room for a specified number of turns

        :param stat: The stat to train
        :param turns: The number of turns to train for
        """
        super().__init__(session)

        params = {"preaction": "gym", "whichgym": gym_stat_mapping[stat], "numturns": turns}
        self.request = session.request("clan_rumpus.php", params=params)

    @staticmethod
    def parser(html: str, url: URL, **kwargs) -> Response:
        stat = gym_stat_mapping[int(url.query["whichgym"])]
        assert isinstance(stat, Stat)

        return Response(
            substats=parsing.substat(html, stat=stat),
            stats=parsing.stat(html, stat=stat),
            level=parsing.level(html),
        )
