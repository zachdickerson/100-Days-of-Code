

console.log("Welcome to Treasure Island.\nYour mission is to find the treasure.")

let road = prompt("You're " + 'at a cross road. Where do you want to go? Type "left" or "right"\n')

if (road === "left") {

    let lake = prompt('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    
    if (lake === "wait") {
        
        let color = prompt('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n')
        
        if (color === 'red') {
            console.log("Burned by fire. Game Over.");

        } else if (color === 'yellow') {
            console.log("You Win!");

        } else if (color === 'blue') {
            console.log("Eaten by beasts. Game Over.");

        } else {
            console.log("Game Over.");
        }
    } else {
        console.log('Attacked by trout. Game Over');
    }



} else {
    console.log("Fall into a hole. Game Over")
}
    

    
