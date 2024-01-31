const student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}
// # 🚨 Don't change the code above 👆
// # TODO-1: Create an empty dictionary called student_grades.
let student_grades = {}
// # TODO-2: Write your code below to add the grades to student_grades.👇
for (const [key, value] of Object.entries(student_scores)) {
    console.log(key, value);
    if (student_scores[key] > 90) {
        student_grades[key] = 'Outstanding'
    } else if (student_scores[key] > 80) {
        student_grades[key] = 'Exceeds Expectations'
    } else if (student_scores[key] > 70) {
        student_grades[key] = 'Acceptable'
    } else {
        student_grades[key] = 'Fail'
    }
}

// # 🚨 Don't change the code below 👇
console.log(student_grades)
