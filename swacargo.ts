class Airport {
	constructor(public code: String,
				public zone: number) {
	}
}

interface Service {
	cost(waybill : Waybill) : number;
}

class Package {

	constructor(public length : number,
				public width : number,
				public height : number,
				public weight : number) {

	}

	getDimensionalWeight() : number {
		var dw : number;
		dw = this.length * this.width * this.height / 194;
		return dw;
	}

	getBillableWeight() : number {
		if (this.getDimensionalWeight() > this.weight) {
			return this.getDimensionalWeight();
		}
		else {
			return this.weight;
		}
	}
}

class InvoiceItem {
	constructor(public description : string,
				public cost : number) {

	}
}


class Waybill {
	constructor(public packages : Package[],
				public origin : Airport,
				public destination : Airport) {

	}

	getTotalWeight() : number {
		var totalWeight = 0;
		for (var i in this.packages) {
			totalWeight += this.packages[i].weight;
		}
		return totalWeight;
	}

	getTotalBillableWeight() : number {
		var totalWeight = 0;
		for (var i in this.packages) {
			totalWeight += this.packages[i].getBillableWeight();
		}
		return totalWeight;
	}

	getFuelSurcharge() : number {
		var weightSurcharge = this.getTotalWeight() * 0.39;
		if (weightSurcharge > 7) {
			return weightSurcharge;
		}
		else {
			return 7;
		}
	}

	getSecuritySurcharge() : number {
		var weightSurcharge = this.getTotalWeight() * 0.06;
		if (weightSurcharge > 6) {
			return weightSurcharge;
		}
		else {
			return 6;
		}
	}

	getSurcharges() : number {
		return this.getSecuritySurcharge() + this.getFuelSurcharge();
	}

	cost(service : Service) : number {
		return this.getSurcharges() + service.cost(this);
	}

	invoice(service : Service) : InvoiceItem[] {
		return [
			new InvoiceItem("Service Charge", service.cost(this)),
			new InvoiceItem("Security Surcharge", this.getSecuritySurcharge()),
			new InvoiceItem("Fuel Surcharge", this.getFuelSurcharge())
		];
	}
}

class Freight implements Service {

	static minimum_table = {
		1: { 1: 45, 2: 45, 3: 45, 4: 45, 5: 45, 6: 50, 7: 50 },
		2: { 1: 45, 2: 45, 3: 45, 4: 45, 5: 45, 6: 45, 7: 45 },
		3: { 1: 45, 2: 45, 3: 45, 4: 45, 5: 45, 6: 50, 7: 50 },
		4: { 1: 45, 2: 45, 3: 45, 4: 45, 5: 45, 6: 45, 7: 45 },
		5: { 1: 45, 2: 45, 3: 45, 4: 45, 5: 45, 6: 45, 7: 45 },
		6: { 1: 50, 2: 45, 3: 50, 4: 45, 5: 45, 6: 45, 7: 45 },
		7: { 1: 50, 2: 45, 3: 50, 4: 45, 5: 45, 6: 45, 7: 45 }
	};

	cost(waybill : Waybill) : number {
		return 50;
	}
}

class RUSH implements Service {

	static minimum_table = {
		1: { 1: 55, 2: 60, 3: 60, 4: 60, 5: 60, 6: 70, 7: 70 },
		2: { 1: 60, 2: 55, 3: 60, 4: 60, 5: 60, 6: 60, 7: 60 },
		3: { 1: 60, 2: 60, 3: 55, 4: 60, 5: 60, 6: 70, 7: 70 },
		4: { 1: 60, 2: 60, 3: 60, 4: 55, 5: 60, 6: 60, 7: 60 },
		5: { 1: 60, 2: 60, 3: 60, 4: 60, 5: 55, 6: 60, 7: 60 },
		6: { 1: 70, 2: 60, 3: 70, 4: 60, 5: 60, 6: 55, 7: 55 },
		7: { 1: 70, 2: 60, 3: 70, 4: 60, 5: 60, 6: 55, 7: 55 }
	};

	static cost_table = {
		1: { 1: 0.68, 2: 0.70, 3: 0.69, 4: 0.73, 5: 0.73, 6: 1.01, 7: 1.01 },
		2: { 1: 0.69, 2: 0.68, 3: 0.69, 4: 0.70, 5: 0.68, 6: 0.73, 7: 0.73 },
		3: { 1: 0.69, 2: 0.69, 3: 0.68, 4: 0.70, 5: 0.71, 6: 1.01, 7: 1.01 },
		4: { 1: 0.73, 2: 0.71, 3: 0.70, 4: 0.69, 5: 0.70, 6: 0.71, 7: 0.73 },
		5: { 1: 0.73, 2: 0.68, 3: 0.71, 4: 0.70, 5: 0.68, 6: 0.71, 7: 0.71 },
		6: { 1: 1.01, 2: 0.73, 3: 1.01, 4: 0.72, 5: 0.75, 6: 0.69, 7: 0.70 },
		7: { 1: 1.01, 2: 0.73, 3: 1.01, 4: 0.73, 5: 0.71, 6: 0.70, 7: 0.68 }
	};

	cost(waybill : Waybill) : number {
		var weight_cost = RUSH.cost_table[waybill.origin.zone][waybill.destination.zone] * waybill.getTotalBillableWeight();
		return Math.max(weight_cost, RUSH.minimum_table[waybill.origin.zone][waybill.destination.zone]);
	}
}

class NFG implements Service {

	static zoning = {
		1: { 1: 'A', 2: 'B', 3: 'B', 4: 'B', 5: 'B', 6: 'C', 7: 'C' },
		2: { 1: 'B', 2: 'A', 3: 'B', 4: 'B', 5: 'B', 6: 'B', 7: 'B' },
		3: { 1: 'B', 2: 'B', 3: 'A', 4: 'B', 5: 'B', 6: 'C', 7: 'C' },
		4: { 1: 'B', 2: 'B', 3: 'B', 4: 'A', 5: 'B', 6: 'B', 7: 'B' },
		5: { 1: 'B', 2: 'B', 3: 'B', 4: 'B', 5: 'A', 6: 'B', 7: 'B' },
		6: { 1: 'C', 2: 'B', 3: 'C', 4: 'B', 5: 'B', 6: 'A', 7: 'A' },
		7: { 1: 'C', 2: 'B', 3: 'C', 4: 'B', 5: 'B', 6: 'A', 7: 'A' }
	};

	static weight_class = {
		'A': [60, 75, 90, 90],
		'B': [70, 80, 95, 95],
		'C': [80, 95, 120, 120]
	};

	static addl_weight = {
		'A': 1.21,
		'B': 1.21,
		'C': 1.32
	}

	cost(waybill : Waybill) : number {
		var billWeight = waybill.getTotalBillableWeight();
		var zone = NFG.zoning[waybill.origin.zone][waybill.destination.zone];
		if (billWeight >= 0 && billWeight < 26) {
			return NFG.weight_class[zone][0];
		}
		else if (billWeight >= 26 && billWeight < 50) {
			return NFG.weight_class[zone][1];
		}
		else if (billWeight >= 50 && billWeight < 100) {
			return NFG.weight_class[zone][2];
		}
		else {
			return NFG.weight_class[zone][3] + (NFG.addl_weight[zone] * (billWeight - 100));
		}
	}
}

var ezWaybill = new Waybill([new Package(26, 26, 26, 40), new Package(26, 26, 26, 40)],
	new Airport('DEN', 5), new Airport('SJC', 6));

console.log('NFG : $' + ezWaybill.cost(new NFG()));
console.log('RUSH: $' + ezWaybill.cost(new RUSH()));
console.log('Frgt: $' + ezWaybill.cost(new Freight()));