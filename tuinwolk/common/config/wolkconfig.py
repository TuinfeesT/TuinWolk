import ConfigParser.SafeConfigParser
from os.path import *
class WolkConfig:

	#TODO: maybe we need more/other configuration locations?
	possible_locations = [ #a list of possible configuration locations, in increasing order of importance
			'/etc/tuinwolkserver/config',
			'~/.config/tuinwolkserver/config',
			'config' #for debugging purposes
			] 

	def __init__(self):
		self.config = SafeConfigParser()
		found = None
		i = 0
		while i < len(possible_locations) and not found:
			loc = possible_locations[i]
			if isFile(loc):
				found = open(loc)
			i += 1
		if found:
			self.config.read(found)




