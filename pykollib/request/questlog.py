import re
from enum import Enum
from typing import Any, Coroutine, Dict

from aiohttp import ClientResponse

import pykollib


class QuestPage(Enum):
    Current = 1
    Completed = 2
    Accomplishments = 3
    Notes = 4
    HoboCode = 5
    MonsterManuel = 6


quests_completed_pattern = re.compile(
    r"<b>([\w\s,\.\'\?!]+)<\/b>(?!<\/td>)<br>([\w\s,\.\'\?!]+)<p>"
)


def parse(html: str, **kwargs) -> Dict[str, str]:
    return {
        match.group(1): match.group(2)
        for match in quests_completed_pattern.finditer(html)
    }


def questlog(session: "pykollib.Session", page: QuestPage = QuestPage.Current) -> Coroutine[Any, Any, ClientResponse]:
    """
    Get info from the quest log about which quests are completed and which stage of each uncompleted quest the player is on
    """

    params = {"which": page.value}
    return session.request("questlog.php", params=params, parse=parse)
