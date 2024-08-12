import unittest

import requests

from app.consts import ContestConsts
from app.contest.parser import ContestParser


class TestContestParser(unittest.TestCase):
	def testGetSessionId(self):
		response = requests.post(ContestConsts.getRequestsUrl())
		self.assertEqual(
			ContestParser.getSessionId(response.content),
			ContestConsts.NON_AUTHENTICATED_SESSION_ID
		)
	
#	def testGetAviableHwCount(self):
#		self.assertTrue(0 <= ContestParser.getAviableHwCount())
#
#	def testAllHomework(self):
#		for index in range(1, ContestParser.getAviableHwCount() + 1):
#			ContestParser.getHomework(index)
