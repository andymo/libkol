from typing import List, NamedTuple

from bs4 import BeautifulSoup

import pykollib

from ..Item import Item
from .request import Request


class Listing(NamedTuple):
    price: int
    quantity: int
    limit: int


class Response(NamedTuple):
    unlimited: List[Listing]
    limited: List[Listing]


class mall_search_price(Request):
    """
    Search the mall for the lowest prices of an item. This will return the
    4 lowest unlimited prices, and if applicable, the 3 lowest limited
    prices with their limit amount per day.

    I'm not sure what the counts when doing a search are, but I'm including it anyways.

    :param session: Active session
    :param item: Item for which to get prices
    """
    def __init__(self, session: "pykollib.Session", item: Item) -> None:
        super().__init__(session)

        data = {"action": "prices", "iid": item.id}
        self.request = session.request("backoffice.php", data=data, pwd=True)

    @staticmethod
    def parser(html: str, **kwargs) -> Response:
        soup = BeautifulSoup(html, "html.parser")

        unlimited = soup.find("td", text="unlimited:")
        limited = soup.find("td", text="limited:")

        return Response(
            unlimited=[
                Listing(int(p.b.string.replace(",", "")), int(p.contents[1][2:]), 0)
                for p in unlimited.find_next_siblings("td")
            ],
            limited=[
                Listing(
                    int(p.b.string.replace(",", "")),
                    int(p.contents[1].split(" ")[1][1:]),
                    int(p.contents[1].split(" ")[0][1:-5]),
                )
                for p in limited.find_next_siblings("td")
            ],
        )