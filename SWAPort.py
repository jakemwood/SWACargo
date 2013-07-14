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
		airports = [
			SWAPort("BOS", 1),
			SWAPort("LGA", 1),
			SWAPort("EWR", 1),
			SWAPort("BWI", 1),
			SWAPort("DEN", 5),
			SWAPort("OMA", 5),
			SWAPort("MSP", 5),
			SWAPort("MCI", 5),
			SWAPort("STL", 5),
			SWAPort("SJC", 6)
		]
		try:
			return next(airport for airport in airports if airport.code == code)
		except StopIteration:
			raise CargoError()