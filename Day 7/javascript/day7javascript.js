
// import { word_list } from './hangman_words.js';

// HangMan
// Randomly Chose a word in the list

const word_list = [
    'abruptly', 
    'absurd', 
    'abyss', 
    'affix', 
    'askew', 
    'avenue', 
    'awkward', 
    'axiom', 
    'azure', 
    'bagpipes', 
    'bandwagon', 
    'banjo', 
    'bayou', 
    'beekeeper', 
    'bikini', 
    'blitz', 
    'blizzard', 
    'boggle', 
    'bookworm', 
    'boxcar', 
    'boxful', 
    'buckaroo', 
    'buffalo', 
    'buffoon', 
    'buxom', 
    'buzzard', 
    'buzzing', 
    'buzzwords', 
    'caliph', 
    'cobweb', 
    'cockiness', 
    'croquet', 
    'crypt', 
    'curacao', 
    'cycle', 
    'daiquiri', 
    'dirndl', 
    'disavow', 
    'dizzying', 
    'duplex', 
    'dwarves', 
    'embezzle', 
    'equip', 
    'espionage', 
    'euouae', 
    'exodus', 
    'faking', 
    'fishhook', 
    'fixable', 
    'fjord', 
    'flapjack', 
    'flopping', 
    'fluffiness', 
    'flyby', 
    'foxglove', 
    'frazzled', 
    'frizzled', 
    'fuchsia', 
    'funny', 
    'gabby', 
    'galaxy', 
    'galvanize', 
    'gazebo', 
    'giaour', 
    'gizmo', 
    'glowworm', 
    'glyph', 
    'gnarly', 
    'gnostic', 
    'gossip', 
    'grogginess', 
    'haiku', 
    'haphazard', 
    'hyphen', 
    'iatrogenic', 
    'icebox', 
    'injury', 
    'ivory', 
    'ivy', 
    'jackpot', 
    'jaundice', 
    'jawbreaker', 
    'jaywalk', 
    'jazziest', 
    'jazzy', 
    'jelly', 
    'jigsaw', 
    'jinx', 
    'jiujitsu', 
    'jockey', 
    'jogging', 
    'joking', 
    'jovial', 
    'joyful', 
    'juicy', 
    'jukebox', 
    'jumbo', 
    'kayak', 
    'kazoo', 
    'keyhole', 
    'khaki', 
    'kilobyte', 
    'kiosk', 
    'kitsch', 
    'kiwifruit', 
    'klutz', 
    'knapsack', 
    'larynx', 
    'lengths', 
    'lucky', 
    'luxury', 
    'lymph', 
    'marquis', 
    'matrix', 
    'megahertz', 
    'microwave', 
    'mnemonic', 
    'mystify', 
    'naphtha', 
    'nightclub', 
    'nowadays', 
    'numbskull', 
    'nymph', 
    'onyx', 
    'ovary', 
    'oxidize', 
    'oxygen', 
    'pajama', 
    'peekaboo', 
    'phlegm', 
    'pixel', 
    'pizazz', 
    'pneumonia', 
    'polka', 
    'pshaw', 
    'psyche', 
    'puppy', 
    'puzzling', 
    'quartz', 
    'queue', 
    'quips', 
    'quixotic', 
    'quiz', 
    'quizzes', 
    'quorum', 
    'razzmatazz', 
    'rhubarb', 
    'rhythm', 
    'rickshaw', 
    'schnapps', 
    'scratch', 
    'shiv', 
    'snazzy', 
    'sphinx', 
    'spritz', 
    'squawk', 
    'staff', 
    'strength', 
    'strengths', 
    'stretch', 
    'stronghold', 
    'stymied', 
    'subway', 
    'swivel', 
    'syndrome', 
    'thriftless', 
    'thumbscrew', 
    'topaz', 
    'transcript', 
    'transgress', 
    'transplant', 
    'triphthong', 
    'twelfth', 
    'twelfths', 
    'unknown', 
    'unworthy', 
    'unzip', 
    'uptown', 
    'vaporize', 
    'vixen', 
    'vodka', 
    'voodoo', 
    'vortex', 
    'voyeurism', 
    'walkway', 
    'waltz', 
    'wave', 
    'wavy', 
    'waxy', 
    'wellspring', 
    'wheezy', 
    'whiskey', 
    'whizzing', 
    'whomever', 
    'wimpy', 
    'witchcraft', 
    'wizard', 
    'woozy', 
    'wristwatch', 
    'wyvern', 
    'xylophone', 
    'yachtsman', 
    'yippee', 
    'yoked', 
    'youthful', 
    'yummy', 
    'zephyr', 
    'zigzag', 
    'zigzagging', 
    'zilch', 
    'zipper', 
    'zodiac', 
    'zombie', 
];

// Length of word_list
const word_list_length = word_list.length;
// Choosing a random word in this array
const chosen_word = word_list[Math.round(Math.random()*word_list_length)];

console.log(chosen_word);

// Chosen Word Length
let chosen_word_length = chosen_word.length

//Creation of Display our "_" array
let display = [];
for (let i = 0; i < chosen_word_length; i++) {
    display += "_";
};

console.log(display);

let lives = 6;
let end_of_game = false;

while (end_of_game != true) {

    let guess = prompt("Please guess a letter: ").toLowerCase();

    // if (display.includes(guess)) {
    //     console.log("You've guessed '" + guess + "', try again.");
    // };

    for (let i = 0; i < chosen_word_length; i++){
        letter = chosen_word[i]
        if (letter === guess) {
            display[i] = guess;
            console.log(display)
        };
    };
    console.log(guess)
    console.log(display)

    if (chosen_word.includes(guess)) {
        console.log("Correct Guess!");
    } else {
        console.log("You've guessed '" + guess + "', this letter is not in the word :(");
        lives -= 1;
        if (lives === 0) {
            end_of_game = true;
            console.log('You lose!');
        };
    };

    display_string = ""
    //console.log(display.join(" "))
    for (let i = 0; i < display.length; i++) {
        display_string += (" " + display[i] + "");
    }

    console.log(display_string)

    //Check if user has got all letters

    if (!(display.includes("_"))) {
        end_of_game = true;
        console.log("You Win.");
    };
    
};

