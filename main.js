var prompt = require('prompt');

// Start the prompt
prompt.start();

var pkg_question = {
	description: 'How many packages are you shipping?',
	type: 'string',
	message: 'Must be a number',
	required: true
};

// Ask how many packages we need...
prompt.get([pkg_question], function(err, pkg_count) {
	console.log(pkg_count);
});