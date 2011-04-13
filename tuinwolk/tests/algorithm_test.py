import random, string, sys

GROWTH_RATE = 2 # we only place repo's in locations that support at least GROWTH_RATE times the size of the repo
CHIP_RATE = 0.9 # if a repo has no locations that support GROWTH_RATE * repo.local_size, we chip off a bit off the desired size to see if we can find a repo anyway
MAX_SERVERS = 10
MAX_LOCATIONS = 10
MAX_REPOS = 10
__test__ = False
class GeoLoc:
	def __init__(self, coords=("", "")):
			self.coords = coords

class Server:

	def __init__(self, ip, port, user, geoloc=GeoLoc()):#, locations=[]): self.geoloc = geoloc self.ip = ip
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

class Repo:

	def __init__(self, name, safe_mode, local_size, min_locations, locations, base_location=None):
		self.name = name
		self.safe_mode = safe_mode
		self.local_size = local_size
		self.min_locations = min_locations
		self.locations = locations
		self.base_location = base_location
	
	def __str__(self):
		return repr(self) #'%7s (%3dMB : %s)' %(self.name, self.local_size, self.min_locations) 

	def __repr__(self):
		return '{0} ({1:5d}MB : {2} sites : based in {3})'.format(self.name, self.commit_size(), self.min_locations, self.base_location) 
	
	def commit_size(self):
		return GROWTH_RATE * self.local_size
	
class Location:

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

def main():
	(servers, repos, locations) = init_test_data()
	run = 0
	while distribute(servers, repos, locations, run):
		print_state(servers)
		run += 1

def distribute(servers, repos, locations, run=0):
	#below is version 0.2 of the distribution protocol.
	placed = False
	#set the base locations
	for repo in repos:
		if repo not in repo.base_location.repos:
			repo.base_location.repos.append(repo)
		if repo.base_location not in repo.locations:
			repo.locations.append(repo.base_location)

	repos = sorted(repos, key=lambda r : r.local_size, reverse=True)
	locations = sorted(locations, key=lambda l : l.max_size - l.committed_size(), reverse=True)

	for repo in repos:
		possible_locations = find_possible_locations(repo, locations)
		print("Will try to place {repo} in {min_loc} of {pos}".format(repo=repo, min_loc=repo.min_locations - len(repo.locations) if run == 0 else 1, pos=possible_locations))
		for placing in (range(repo.min_locations - 1) if run == 0 else [0]):
			if len(possible_locations) > 0:
				print("Placing {repo} in {loc}".format(repo=repo, loc=possible_locations[-1]))
				placed = True
				repo.locations.append(possible_locations[-1])
				possible_locations[-1].repos.append(repo)
				possible_locations = possible_locations[:-1]
			elif run == 0:
				print('wine!')
				break
	return placed

def init_test_data():
	servers = []
	for i in range(MAX_SERVERS):
		s = Server(ip='ip_' + str(i), port=random.randint(1024,65535), user=random_str(5))
		servers.append(s)

	locations = []
	for i in range(MAX_LOCATIONS):
		locations.append(Location(max_up=random.randint(0,500), max_down=random.randint(0,500), max_size=random.randint(1000,100000), path="/" + random_str(4), server=random.choice(servers)))

	repos = []
	for i in range(MAX_REPOS):
		repos.append(Repo(name='repo_' + str(i), safe_mode=i % 3 == 0, local_size=int(1.02 ** random.randint(100,550)), min_locations=i % 3 + 1, locations=[]))

	for repo in repos:
		locs = find_possible_locations(repo, locations)
		if len(locs) > 0:
			loc = random.choice(locs)
			repo.base_location=loc
			repo.locations.append(repo.base_location)
			loc.repos.append(repo)
		else:
			print("testset broken")
			sys.exit(-1)

	print_state(servers)
	return (servers, repos, locations)

def random_str(number):
	return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(number))

def find_possible_locations(repo, locations):
	result = []
	for loc in locations:
		serv_repos = []
		for l in loc.server.locations:
			serv_repos += l.repos

		if repo not in serv_repos and (loc.max_size - loc.committed_size()) > repo.commit_size():
			result.append(loc)
	return result


def print_state(s):
	print('Servers:')
	if type(s) == list:
		for serv in s:
			print(serv)
	else:
		print(s)
	print("*"*200)

if __name__ == '__main__':
	main()

