const target = 10;

let total = 0;
const new_tar = target + 1;

for (let i = 0; i < new_tar; i++) {
    if (i % 2 == 0) {
        total+=i;
    }  
};

console.log(total);