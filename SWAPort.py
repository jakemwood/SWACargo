from interfaces import Airport, CargoError

"""
Southwest airports are affiliated with a zone.  As such, we'll
extend the Airport class to also have a zone.
"""
class SWAPort(Airport):
	def __init__(self, code, zone):
		self.code = code
		self.zone = zone

	@staticmethod
	def code_to_airport(code):
		# This is the list of Southwest airports based on their map...
		# http://www.swacargo.com/swacargo/documents/2013CargoMap_AllDest-Zoned.pdf
		airports = [
			SWAPort("BOS", 1),
			SWAPort("LGA", 1),
			SWAPort("EWR", 1),
			SWAPort("BWI", 1),
			SWAPort("DEN", 5), # Denver
			SWAPort("OMA", 5), # Omaha
			SWAPort("MSP", 5), # Minneapolis / St Paul
			SWAPort("MCI", 5), # Kansas City
			SWAPort("STL", 5), # St Louis
			SWAPort("SMF", 6), # Sacramento
			SWAPort("SFO", 6), # San Francisco
			SWAPort("OAK", 6), # Oakland
			SWAPort("SJC", 6), # San Jose
			SWAPort("BUR", 6), # Burbank
			SWAPort("LAX", 6), # Los Angeles
			SWAPort("ONT", 6), # Ontario, California
			SWAPort("SNA", 6), # Orange County Airport
			SWAPort("SAN", 6), # San Diego
			SWAPort("RNO", 6), # Reno / Tahoe
			SWAPort("LAS", 6), # Las Vegas
			SWAPort("SLC", 6), # Salt Lake City
			SWAPort("PHX", 6), # Phoenix
			SWAPort("TUS", 6), # Tucson
			SWAPort("SEA", 7), # Seattle
			SWAPort("GEG", 7), # Spokane
			SWAPort("PDX", 7), # Portland
			SWAPort("BOI", 7), # Boise
			SWAPort("YVR", 7), # Vancouver
			SWAPort("YEG", 7), # Edmonton
			SWAPort("YYC", 7) # Calgary
		]
		try:
			return next(airport for airport in airports if airport.code == code)
		except StopIteration:
			raise CargoError()