
function prime_check(num) {
    
    let is_prime = true;

    for (let i = 2; i < num; i++) {
        if (num % i == 0) {
            is_prime = false;
        };
    };
    if (is_prime === true) {
        console.log("It is a prime number.");
    } else {
        console.log("It's not a prime number.");
    };
};

prime_check(87);
prime_check(97);
prime_check(66);
prime_check(47);