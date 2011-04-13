import git
class WolkRepo:
	def __init__(self, name, safe_mode, local_size, min_locations, locations, base_location):
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


