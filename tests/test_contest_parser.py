import unittest

import requests

from csti.consts import ContestConsts
from csti.contest import ContestParser


class TestContestParser(unittest.TestCase):
	def testGetSessionId(self):
		response = requests.post(ContestConsts.getRequestsUrl())
		self.assertEqual(
			ContestParser.getSessionId(response.content),
			ContestConsts.NON_AUTHENTICATED_SESSION_ID
		)
