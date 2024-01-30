let line1 = ["⬜️","️⬜️","️⬜️"];
let line2 = ["⬜️","⬜️","️⬜️"];
let line3 = ["⬜️️","⬜️️","⬜️️"];
let map = [line1, line2, line3]
console.log("Hiding your treasure! X marks the spot.")

const position = 'A1';

letter = position[0].toLowerCase();

const abc = ['a','b','c']

index_letter = abc.indexOf(letter);

index_number = position[1] - 1

map[index_number][index_letter] = 'X'

console.log(line1 + '\n' + line2 +'\n' + line3)
