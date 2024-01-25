const computer = random.randint(0,2);

const human = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"));

if (human >=3 || computer < 0) {
    console.log('You typed an invalid number, you lose!');
} else {
    console.log("Computer chose:\n" + computer);

    if (human === computer) {
        console.log("Draw! Try Again.");
    } else if (human == 0 && computer == 1) {
        console.log('You Lose!');
    } else if (human == 0 && computer == 2){
        console.log('You Win!');
    } else if (human == 1 && computer == 0){
        console.log('You Win!');
    } else if (human == 1 && computer == 2){
        console.log('You Lose!');
    } else if (human == 2 && computer == 0){
        console.log('You Lose!');
    } else if (human == 2 && computer == 1){
        console.log('You Win!');
    } else {
        console.log("Invalid Input");
    }
    
};