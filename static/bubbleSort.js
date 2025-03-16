let arr = [];
let i = 0;
let p = 1;



function setup(){
  createCanvas(600,400);
  for(let i = 0; i < width/10; i++){
    arr.push(random(height))
  }
}
function draw(){
    background(10);
    let temp = 0;
    if(i < arr.length){
        for(p; p < arr.length - i; p++){
            if(arr[p-1] > arr[p]){
                temp = arr[p-1];
                arr[p-1] = arr[p];
                arr[p] = temp
            }
        }
    }
    for(let b = 0; b < arr.length; b++){
        fill(255);
        rect(b*10, height - arr[b], 9, arr[b]);
    }
  }