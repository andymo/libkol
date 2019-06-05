import pykollib

from ..Item import Item
from .request import Request


class item_use(Request):
    """
    Uses the requested item.
    """
    def __init__(self, session: "pykollib.Session", item: Item) -> None:
        super().__init__(session)

        params = {"whichitem": item.id}
        self.request = session.request("inv_use.php", params=params)