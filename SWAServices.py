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

	minimum_table = {
		1: { 1: 45, 2: 45, 3: 45, 4: 45, 5: 45, 6: 50, 7: 50 },
		2: { 1: 45, 2: 45, 3: 45, 4: 45, 5: 45, 6: 45, 7: 45 },
		3: { 1: 45, 2: 45, 3: 45, 4: 45, 5: 45, 6: 50, 7: 50 },
		4: { 1: 45, 2: 45, 3: 45, 4: 45, 5: 45, 6: 45, 7: 45 },
		5: { 1: 45, 2: 45, 3: 45, 4: 45, 5: 45, 6: 45, 7: 45 },
		6: { 1: 50, 2: 45, 3: 50, 4: 45, 5: 45, 6: 45, 7: 45 },
		7: { 1: 50, 2: 45, 3: 50, 4: 45, 5: 45, 6: 45, 7: 45 }
	}

	cost_table = {
		1: { 1: 0.51, 2: 0.59, 3: 0.58, 4: 0.63, 5: 0.61, 6: 0.93, 7: 0.93 },
		2: { 1: 0.58, 2: 0.51, 3: 0.58, 4: 0.59, 5: 0.55, 6: 0.63, 7: 0.63 },
		3: { 1: 0.58, 2: 0.58, 3: 0.50, 4: 0.57, 5: 0.62, 6: 0.93, 7: 0.93 },
		4: { 1: 0.63, 2: 0.62, 3: 0.59, 4: 0.58, 5: 0.59, 6: 0.63, 7: 0.64 },
		5: { 1: 0.61, 2: 0.55, 3: 0.62, 4: 0.59, 5: 0.51, 6: 0.63, 7: 0.63 },
		6: { 1: 0.93, 2: 0.63, 3: 0.93, 4: 0.64, 5: 0.63, 6: 0.51, 7: 0.51 },
		7: { 1: 0.93, 2: 0.64, 3: 0.93, 4: 0.63, 5: 0.63, 6: 0.50, 7: 0.48 }
	}

	@staticmethod
	def ratePackage(waybill, package):
		if (package.billableWeight() > 300):
			# use the 300 pound table
			multiplier = Freight.cost_table[waybill.origin.zone][waybill.destination.zone] - 0.03
		else:
			# use the cheaper table
			multiplier = Freight.cost_table[waybill.origin.zone][waybill.destination.zone]

		return max(multiplier * package.billableWeight(), \
			Freight.minimum_table[waybill.origin.zone][waybill.destination.zone])

	@staticmethod
	def invoice(waybill):
		packages = []
		for package in waybill.packages:
			packages.append(InvoiceLine("Freight Service", Freight.ratePackage(waybill, package)))
		return packages