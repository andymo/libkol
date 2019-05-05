from .GenericRequest import GenericRequest
from pykollib.util import ParseResponseUtils


class MeatOrchidRequest(GenericRequest):
    "Visits the hanging meat orchid in the clan rumpus room."

    def __init__(self, session):
        super(MeatOrchidRequest, self).__init__(session)
        self.url = session.server_url + "clan_rumpus.php?action=click&spot=1&furni=4"

    def parseResponse(self):
        self.responseData["meat"] = ParseResponseUtils.parseMeatGainedLost(
            self.responseText
        )
