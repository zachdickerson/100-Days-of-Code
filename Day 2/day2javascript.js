/*
"Hello"[1];  == "e"

How to Round in Java Script

Math.round(5.685 * 100) / 100    this equals   5.69

*/

console.log("Welcome to the tip calculator.");
const total = prompt('What was the total bill? $');
const percent = prompt('What percentage tip would you like to give? 10, 12, or 15? ');
const people = prompt('How many people to split the bill? ');

let percent_price = total * (percent/100);
let total_tip = total + percent_price;
let the_split = total_tip / people;
let rounded_split = Math.round(the_split * 100) / 100;

print('Each person should pay: $${rounded_split}');