from interfaces import Service, InvoiceLine

class NextFlight(Service):

	zoning = {
		1: { 1: 'A', 2: 'B', 3: 'B', 4: 'B', 5: 'B', 6: 'C', 7: 'C' },
		2: { 1: 'B', 2: 'A', 3: 'B', 4: 'B', 5: 'B', 6: 'B', 7: 'B' },
		3: { 1: 'B', 2: 'B', 3: 'A', 4: 'B', 5: 'B', 6: 'C', 7: 'C' },
		4: { 1: 'B', 2: 'B', 3: 'B', 4: 'A', 5: 'B', 6: 'B', 7: 'B' },
		5: { 1: 'B', 2: 'B', 3: 'B', 4: 'B', 5: 'A', 6: 'B', 7: 'B' },
		6: { 1: 'C', 2: 'B', 3: 'C', 4: 'B', 5: 'B', 6: 'A', 7: 'A' },
		7: { 1: 'C', 2: 'B', 3: 'C', 4: 'B', 5: 'B', 6: 'A', 7: 'A' }
	};

	weight_class = {
		'A': [60, 75, 90, 90],
		'B': [70, 80, 95, 95],
		'C': [80, 95, 120, 120]
	};

	addl_weight = {
		'A': 1.21,
		'B': 1.21,
		'C': 1.32
	}

	@staticmethod
	def ratePackage(waybill, package):
		billWeight = package.billableWeight()
		zone = NextFlight.zoning[waybill.origin.zone][waybill.destination.zone]
		if billWeight >= 0 and billWeight < 26:
			return NextFlight.weight_class[zone][0]
		elif billWeight >= 26 and billWeight < 50:
			return NextFlight.weight_class[zone][1]
		elif billWeight >= 50 and billWeight < 100:
			return NextFlight.weight_class[zone][2]
		else:
			return NextFlight.weight_class[zone][3] + (NextFlight.addl_weight[zone] * (billWeight - 100))
		return 0

	@staticmethod
	def invoice(waybill):
		packages = []
		for package in waybill.packages:
			packages.append(InvoiceLine("Next Flight Guarantee Service", NextFlight.ratePackage(waybill, package)))
		return packages

class Rush(Service):

	minimum_table = {
		1: { 1: 55, 2: 60, 3: 60, 4: 60, 5: 60, 6: 70, 7: 70 },
		2: { 1: 60, 2: 55, 3: 60, 4: 60, 5: 60, 6: 60, 7: 60 },
		3: { 1: 60, 2: 60, 3: 55, 4: 60, 5: 60, 6: 70, 7: 70 },
		4: { 1: 60, 2: 60, 3: 60, 4: 55, 5: 60, 6: 60, 7: 60 },
		5: { 1: 60, 2: 60, 3: 60, 4: 60, 5: 55, 6: 60, 7: 60 },
		6: { 1: 70, 2: 60, 3: 70, 4: 60, 5: 60, 6: 55, 7: 55 },
		7: { 1: 70, 2: 60, 3: 70, 4: 60, 5: 60, 6: 55, 7: 55 }
	}

	cost_table = {
		1: { 1: 0.68, 2: 0.70, 3: 0.69, 4: 0.73, 5: 0.73, 6: 1.01, 7: 1.01 },
		2: { 1: 0.69, 2: 0.68, 3: 0.69, 4: 0.70, 5: 0.68, 6: 0.73, 7: 0.73 },
		3: { 1: 0.69, 2: 0.69, 3: 0.68, 4: 0.70, 5: 0.71, 6: 1.01, 7: 1.01 },
		4: { 1: 0.73, 2: 0.71, 3: 0.70, 4: 0.69, 5: 0.70, 6: 0.71, 7: 0.73 },
		5: { 1: 0.73, 2: 0.68, 3: 0.71, 4: 0.70, 5: 0.68, 6: 0.71, 7: 0.71 },
		6: { 1: 1.01, 2: 0.73, 3: 1.01, 4: 0.72, 5: 0.75, 6: 0.69, 7: 0.70 },
		7: { 1: 1.01, 2: 0.73, 3: 1.01, 4: 0.73, 5: 0.71, 6: 0.70, 7: 0.68 }
	}

	@staticmethod
	def ratePackage(waybill, package):
		weight_cost = Rush.cost_table[waybill.origin.zone][waybill.destination.zone] * package.billableWeight()
		return max(weight_cost, Rush.minimum_table[waybill.origin.zone][waybill.destination.zone])

	@staticmethod
	def invoice(waybill):
		packages = []
		for package in waybill.packages:
			packages.append(InvoiceLine("RUSH Guarantee Service", Rush.ratePackage(waybill, package)))
		return packages

class Freight(Service):
	@staticmethod
	def cost(waybill):
		return 0