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
		invoice.append(InvoiceLine("Fuel Surcharge", self.fuelSurcharge()))
		# Based on the quote I received from the SWA rep, the security
		# surcharge is not included in the federal tax.
		invoice.append(InvoiceLine("Federal Tax - 6.25%", 0.0625 * sum(line.charge for line in invoice)))
		invoice.append(InvoiceLine("Security Surcharge", self.securitySurcharge()))

		return invoice