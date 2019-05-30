from typing import Any, Coroutine, NamedTuple

from aiohttp import ClientResponse

import pykollib

from ..Error import CannotChangeClanError


class Response(NamedTuple):
    success: bool
    already_member: bool


def parse(html: str, session: "pykollib.Session", **kwargs) -> Response:
    """
    Formats the clan application response
    """

    if (
        "You can't apply to a new clan when you're the leader of an existing clan."
        in html
    ):
        raise CannotChangeClanError(
            "Cannot apply to another clan because you are the leader of {}".format(
                session.state.get("clan_name", "unknown")
            )
        )

    accepted = "clanhalltop.gif" in html
    already_member = "You can't apply to a clan you're already in." in html

    return Response(accepted or already_member, already_member)


def clan_apply(session: "pykollib.Session", clan_id: int) -> Coroutine[Any, Any, ClientResponse]:
    """
    Apply to a clan

    :param clan_id: id of clan
    """

    payload = {
        "recruiter": 1,
        "pwd": session.pwd,
        "whichclan": clan_id,
        "action": "joinclan",
        "apply": "Apply+to+this+Clan",
        "confirm": "on",
    }

    return session.request("showclan.php", data=payload, parse=parse)
