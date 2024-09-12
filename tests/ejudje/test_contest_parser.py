import unittest

import requests

from csti.contest_systems.ejudje.parser import ContestParser
from csti.contest_systems.ejudje.api import EjudjeAPI


class TestContestParser(unittest.TestCase):
    def testGetSessionId(self):
        response = requests.post(EjudjeAPI.REQUEST_URL)
        self.assertEqual(
            ContestParser.getSessionId(response.content),
            EjudjeAPI.BAD_SESSION_ID
        )
