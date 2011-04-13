import unittest, time
from ..server.daemons.infinite_timer import InfiniteTimer
import logging
import os


class TestInfiniteTimerFunctions(unittest.TestCase):

	def setUp(self):
		global returnval
		returnval = False

	def test_timer(self):
		global t
		t = InfiniteTimer(1, self.returnTrue)
		t.start()
		time.sleep(2)
		self.assertTrue(returnval)

	def test_cancel(self):
		global t
		t = InfiniteTimer(4, self.returnTrue)
		t.start()
		time.sleep(2)
		t.cancel()
		self.assertFalse(returnval)
	
	def tearDown(self):
		t.cancel()


	def returnTrue(self):
		global returnval
		returnval = True

if __name__ == '__main__':
	unittest.main()
