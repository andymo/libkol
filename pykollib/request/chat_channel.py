import re
import pykollib

from ..Error import UnknownError
from .request import Request

current_channel_pattern = re.compile(
    '<font color="?#?\w+"?>Currently in channel: ([^<>]+)<'
)

class chat_channel(Request):
    def __init__(self, session: "pykollib.Session") -> None:
        super().__init__(session)
        self.request = session.request("lchat.php")

    @staticmethod
    def parser(html: str, **kwargs) -> str:
        match = current_channel_pattern.search(html)

        if match is None:
            raise UnknownError("Could not parse chat channel")

        return match.group(1)
