#!/usr/bin/node
const files = require('fs');
files.readFile(process.argv[2], 'utf8', function (error, content) {
	  console.log(error || content);
});
