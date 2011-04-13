import unittest, time
from ..server.daemons.infinite_timer import InfiniteTimer

class TestInfiniteTimerFunctions(unittest.TestCase):

	def setUp(self):
		global returnval
		returnval = False

	def test_timer(self):
		print 1
		t = InfiniteTimer(1, self.returnTrue)
		t.start()
		time.sleep(2)
		self.assertTrue(returnval)

	def test_cancel(self):
		print 2
		t = InfiniteTimer(10, self.returnTrue)
		t.start()
		time.sleep(1)
		t.cancel()
		self.assertFalse(returnval)


	def returnTrue(self):
		global returnval
		returnval = True

if __name__ == '__main__':
	unittest.main()
