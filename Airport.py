class Airport:
	def __init__(self, code, zone):
		self.code = code
		self.zone = zone

	@staticmethod
	def airports():
		return [Airport("DEN", 5),
			Airport("DEN", 6)]
