let arr = [];
let i = 1;
let p = 0;



function setup(){
  createCanvas(600,400);
  for(let i = 0; i < width/10; i++){
    arr.push(random(height))
  }
}
function draw(){
    background(10);
    
    for(let b = 0; b < arr.length; b++){
        fill(255);
        rect(b*10, height - arr[b], 9, arr[b]);
    }
  }
