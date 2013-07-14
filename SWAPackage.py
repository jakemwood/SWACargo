from interfaces import Package

class SWAPackage(Package):
	def dimensionalWeight(self):
		return self.length * self.width * self.height / 194

	def billableWeight(self):
		if (self.dimensionalWeight() > self.weight):
			return self.dimensionalWeight()
		else:
			return self.weight