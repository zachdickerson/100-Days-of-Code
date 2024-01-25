// This is the FizzBuzz problem in javascript

const target= 101;

for (let i = 1; i < target; i++) {

    if (i % 3 === 0 && i % 5 == 0) {
        console.log('FizzBuzz');
    } else if (i % 3 === 0) {
        console.log('Fizz');
    } else if (i % 5 == 0) {
        console.log('Buzz');
    } else {
        console.log(i);
    };
};