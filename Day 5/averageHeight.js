// Input a JavaScript list of student heights
let student_heights = [180, 124, 165, 173, 189, 169, 146];


let number_of_students = 0;
let total_height = 0;

for (let i = 0; i < student_heights.length; i++) {
    total_height += student_heights[i];
    number_of_students += 1;
    
};
// console.log(total_height) 
// console.log(number_of_students)

let average_height = Math.round(total_height / number_of_students);

console.log('total height = ' + total_height);
console.log('number of students = ' + number_of_students);
console.log('average height = ' + average_height);