"""
Airport interface for the most basic information about an airport - its code
"""
class Airport:
	def __init__(self, code):
		self.code = code

"""
A class of cargo service offered by an airline
"""
class Service():
	def cost(waybill):
		pass

"""
A package abstract class
"""
class Package:
	def __init__(self, length, width, height, weight):
		self.length = length
		self.width = width
		self.height = height
		self.weight = weight

	def billableWeight(self):
		pass

"""
A line item of an invoice
"""
class InvoiceLine:
	def __init__(self, description, charge):
		self.description = description
		self.charge = charge

"""
A waybill abstract class
"""
class Waybill:
	def __init__(self, origin, destination, packages):
		self.origin = origin
		self.destination = destination
		self.packages = packages

	def totalWeight(self):
		return sum(package.weight for package in self.packages)

	def billableWeight(self):
		return sum(package.billableWeight() for package in self.packages)

	def invoice(self):
		pass

class CargoError(Exception):
	pass