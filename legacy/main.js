var prompt = require('prompt');
require('./swacargo.js');

// Start the prompt
prompt.start();

var pkg_question = {
	name: 'pkg_count',
	description: 'How many packages are you shipping?',
	type: 'string',
	message: 'Must be a number',
	required: true
};

var origin = {
	name: 'origin',
	description: 'Origin airport code',
	type: 'string',
	message: 'Must be a string',
	required: true
};

var destination = {
	name: 'destination',
	description: 'Destination airport code',
	type: 'string',
	message: 'Must be a string',
	required: true
};

// global variable to store packages. Grumble.
var packages = [];

var questions = [origin, destination, pkg_question];

function askPackages(pkg_count) {
	var questions = [];
	for (var i = 1; i <= pkg_count; i++) {
		questions.push({ name: 'len_' + (i - 1), description: "Length of package " + i, required: true });
		questions.push({ name: 'wid_' + (i - 1), description: "Width  of package "  + i, required: true });
		questions.push({ name: 'hgt_' + (i - 1), description: "Height of package " + i, required: true });
		questions.push({ name: 'wgt_' + (i - 1), description: "Weight of package " + i, required: true });
	}
	return questions;
}

function convertPackages(pkg_data) {
	var len = Object.keys(pkg_data).length / 4;
	var packages = [];
	for (var i = 0; i < len; i++) {
		packages.push(new Package(pkg_data['len_' + i], pkg_data['wid_' + i], pkg_data['hgt_'], pkg_data['wgt_']));
	}
	return packages;
}

// Ask how many packages we need...
prompt.get(questions, function(err, basic_info) {
	prompt.get(askPackages(basic_info.pkg_count), function(err, pkg_data) {
		console.log(convertPackages(pkg_data));
		new Waybill()
	});
});
