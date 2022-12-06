const fs = require('fs')
let x = 0;
let y = 0;
let a = 0;

const inp = fs.readFileSync('./input.txt', 'utf8').toString().split("\n").map((i)=>i.split(" ")).forEach(l=>{
    if(l[0]==='forward'){
        x+=Number(l[1]);
        y+=a * Number(l[1]);
    }
    if(l[0]==='down'){
        //y-=Number(l[1]);
        a+=Number(l[1])
    }
    if(l[0]==='up'){
        //y+=Number(l[1]);
        a-=Number(l[1])
    }
    if(l[0]==='backward'){
        x-=Number(l[1]);
    }
})

console.log(y, x, y* x)

