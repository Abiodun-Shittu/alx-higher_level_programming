#!/usr/bin/node
if (process.argv.length <= 3) {
	console.log("0");
} else {
	let arr = process.argv.slice(2).map(Number);
	console.log(arr.sort()[arr.length - 2]);
}
