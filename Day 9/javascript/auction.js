
let keep_going = true;
let bidders = {};

console.log("Welcome to the secret auction program.");

function highest_bid() {
    let count = 0;
    let high_key = "";

    for (const [key, value] of Object.entries(bidders)) {
        if (value > count) {
            count = value;
            high_key = key;
        };
    };
    console.log("The winner is " + high_key + " with a bid of $" + count + ".");
}

while (keep_going) {

    let name_1 = prompt("What is your name? ");
    let bid = Number(prompt("What is your bid? $"));

    bidders[name_1] = bid;

    let keep_pushing = prompt("Are there any other bidders? Type 'yes' or 'no'.");

    if (keep_pushing == 'no') {
        keep_going = false;
        highest_bid();
    }; 
};
