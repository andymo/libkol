from typing import List

import pykollib

from ..Item import ItemQuantity
from ..util import parsing
from .request import Request


class clan_vip_lookingglass(Request):
    def __init__(self, session: "pykollib.Session") -> None:
        """
        Uses the Looking Glass in the clan VIP room.
        """
        super().__init__(session)

        params = {"action": "lookingglass"}
        self.request = session.request("clan_viplounge.php", params=params)

    @staticmethod
    def parser(html: str, **kwargs) -> List[ItemQuantity]:
        return parsing.item(html)
