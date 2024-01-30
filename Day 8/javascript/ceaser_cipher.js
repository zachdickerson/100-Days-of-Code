const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

function caesar(start_text, shift_amount, cipher_direction) {
    let end_text = "";

    if (cipher_direction === "decode") {
        shift_amount *= -1;
    };

    for (let char = 0; char < start_text.lenght; char++) {
        if (alphabet.includes(start_text[char])) {
            let position = alphabet.indexOf(start_text[char]);
            let new_position = position + shift_amount;
            end_text += alphabet[new_position]
        } else {
            end_text += start_text[char];
        };
    };
    console.log(end_text)
    console.log("Here's the " + cipher_direction +"d result: " + end_text);
};

// Import and print the logo from art.py when the program starts.
// import art
// print(art.logo)

let cipher = true;

while (cipher) {
   

    let direction = prompt("Type 'encode' to encrypt, type 'decode' to decrypt:\n");
    let text = prompt("Type your message:\n").toLowerCase();
    let shift = Number(prompt("Type the shift number:\n"));

    shift = shift % 26;
  

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction);

    let proceed = prompt("Type 'yes' if you want to go again. Otherwise type 'no'.\n");

    if (proceed === 'no') {
        cipher = false;
        console.log('Goodbye!');
    };     
};