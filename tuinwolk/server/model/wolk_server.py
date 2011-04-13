class Server:
	def __init__(self, ip, port, user, geoloc=GeoLoc()):#, locations=[]):
		self.geoloc = geoloc
		self.ip = ip
		self.port = port
		self.user = user
		self.geoloc = geoloc
		self.locations = []

	def __str__(self):
		return repr(self)
	
	def __repr__(self):
		s = '{ip}:{port:5}\n'.format(ip=self.ip, port=self.port)
		for loc in self.locations:
			s += '\t{loc}\n'.format(loc=loc)
			for repo in loc.repos:
				s += '\t\t{repo}\n'.format(repo=repo)
		return s
