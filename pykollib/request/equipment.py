from typing import Optional, NamedTuple

from .request import Request
from bs4 import BeautifulSoup, Tag

import pykollib

from ..Item import Item

class Outfit(NamedTuple):
    hat: Optional[Item]
    back: Optional[Item]
    shirt: Optional[Item]
    weapon: Optional[Item]
    offhand: Optional[Item]
    pants: Optional[Item]
    acc1: Optional[Item]
    acc2: Optional[Item]
    acc3: Optional[Item]
    familiar: Optional[Item]

class equipment(Request):
    def __init__(self, session: "pykollib.Session") -> None:
        """
        Gets info on all equipment currently equipped.
        Returns a lookup from the item database for each item equipped.
        For accessories, two possibilities are present.  If equipping each slot seperately is enabled, each item's dictionary will contain an attribute "slot" with the number of the slot it occupies.  Otherwise, the "slot" attribute will have the value 0 for all equipped accessories.
        """
        super().__init__(session)

        params = {"which": 2}
        self.request = session.request("inventory.php", params=params)

    @staticmethod
    def slot_to_item(soup: Tag, link: str, index: int = 0) -> Optional[Item]:
        slot_title = soup.find_all("a", href="#{}".format(link))

        if len(slot_title) == 0:
            return None

        descid = slot_title[index].parent.next_sibling.img["rel"]
        return Item.get_or_none(desc_id=descid)

    @classmethod
    def parser(cls, html: str, **kwargs) -> Outfit:
        soup = BeautifulSoup(html, "html.parser")
        current = soup.find(id="curequip")

        return Outfit(
            hat=cls.slot_to_item(current, "Hats"),
            back=cls.slot_to_item(current, "Back"),
            shirt=cls.slot_to_item(current, "Shirts"),
            weapon=cls.slot_to_item(current, "Weapons"),
            offhand=cls.slot_to_item(current, "Off-Hand"),
            pants=cls.slot_to_item(current, "Pants"),
            acc1=cls.slot_to_item(current, "Accessories", 0),
            acc2=cls.slot_to_item(current, "Accessories", 1),
            acc3=cls.slot_to_item(current, "Accessories", 2),
            familiar=cls.slot_to_item(current, "Familiar"),
        )
