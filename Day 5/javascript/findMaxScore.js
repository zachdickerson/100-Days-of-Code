// Input a list of student scores
const student_scores = [78, 65, 89, 86, 55, 91, 64, 89];

// Write your code below this row 👇

let max = 0;

for (let i = 0; i < student_scores.length; i++) {
    if (student_scores[i] > max) {
        max = student_scores[i];
    }
};

console.log('The highest score in the class is: ' + max);