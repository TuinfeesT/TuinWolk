import random, string
class Repo:
	name = ''
	safe_mode = False
	local_size = 0
	min_locations = 0
	locations = []

	def __init__(self, name, safe_mode, local_size, min_locations, locations):
		self.name = name
		self.safe_mode = safe_mode
		self.local_size = local_size
		self.min_locations = min_locations
		self.locations = locations
	
	def __str__(self):
		return '%7s (%3dMB : %s)' %(self.name, self.local_size, self.min_locations) 

	def __repr__(self):
		return '%7s (%3dMB : %s)' %(self.name, self.local_size, self.min_locations) 
	
class Location:
	ip = ''
	port = 8888
	max_up = 0
	max_down = 0
	max_size = 500
	user = ''
	repos = []

	def __init__(self, ip, port, max_up, max_down, max_size, user):
		self.ip = ip
		self.port = port
		self.max_up = max_up
		self.max_down = max_down
		self.max_size = max_size
		self.user = user

	def __str__(self):
		return '%s@%s:%d(%dMB)' % (self.user, self.ip, self.port, self.max_size)

	def __repr__(self):
		return '%s@%s:%d(%dMB)' % (self.user, self.ip, self.port, self.max_size)

def main():
	(repos, locations) = init_test_data()
	distribute(repos, locations)

def distribute(repos, locations):
	#we start with giving the biggest location the biggest repo
	#then the second biggest location the second biggest repo, etc
	#if a repo doesn't fit, put it in one locatoin bigger
	repos = sorted(repos, key=lambda r : r.local_size, reverse=True)
	locations = sorted(locations, key=lambda l : l.max_size, reverse=True)
	i = 0
	for repo in repos:
		print i
		for _ in range(repo.min_locations):
			print i
			saved_i = i
			if i < len(locations):
				print('Trying to couple %s to %s' % (repo, locations[i]))
				if repo.local_size < locations[i].max_size:
					#we have a match, couple the location
					repo.locations.append(locations[i])
					print('Repo %s coupled to %s' % (repo, locations[i]))
				i -= 1
				i = saved_i if i < saved_i - 1 else saved_i + 1 #to make sure that every location gets a repo

def init_test_data():
	locations = []
	for i in range(10):
		locations.append(Location('ip_'+str(i),random.randint(1024,65535), random.randint(0,500), random.randint(0,500), random.randint(100,300), random_str(5)))

	repos = []
	for i in range(10):
		repos.append(Repo('repo_' + str(i), i % 3, random.randint(1,200), i % 3 + 1, []))
	return (repos, locations)

def random_str(number):
	return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(number))

if __name__ == '__main__':
	main()

