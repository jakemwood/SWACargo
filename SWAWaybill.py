from interfaces import Waybill, InvoiceLine

class SWAWaybill(Waybill):
	def __init__(self, origin, destination, service, packages):
		self.origin = origin
		self.destination = destination
		self.service = service
		self.packages = packages

	def fuelSurcharge(self):
		surcharge = self.totalWeight() * 0.39
		return max(surcharge, 7)

	def securitySurcharge(self):
		surcharge = self.totalWeight() * 0.06
		return max(surcharge, 6)

	def invoice(self):
		invoice = self.service.invoice(self)
		invoice.append(InvoiceLine("Security Surcharge", self.securitySurcharge()))
		invoice.append(InvoiceLine("Fuel Surcharge", self.fuelSurcharge()))

		return invoice