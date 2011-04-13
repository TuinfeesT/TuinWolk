class WolkLocation:

	def __init__(self, max_up, max_down, max_size, path, server):
		self.max_up = max_up
		self.max_down = max_down
		self.max_size = max_size
		self.path = path
		self.server = server
		self.server.locations.append(self)
		self.repos = []

	def __str__(self):
		return repr(self) #'%s@%s:%d(%dMB)' % (self.user, self.ip, self.port, self.max_size)

	def __repr__(self):
		return '{path} @ {ip}({size_left:5}MB of {max_size:5}MB left)'.format(path=self.path, ip=self.server.ip, size_left=self.max_size - self.committed_size(), max_size=self.max_size)
	
	def committed_size(self):
		return sum([r.commit_size() for r in self.repos])
