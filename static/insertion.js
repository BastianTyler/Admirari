let arr = [];
let i = 0;
let p = 0;



function setup(){
  createCanvas(600,400);
  for(let i = 0; i < width/10; i++){
    arr.push(random(height))
  }
  frameRate(5)
}
function draw(){
  background(10);
  
  
  if(i < arr.length - 1){
    key = arr[i];
    p = i - 1
    while(p > 0 && arr[p] > key){
      arr[p + 1] = arr[p];
      p--;
    }
    arr[p+1] = key;
  }
  i++;
  
  for(let b = 0; b < arr.length; b++){
        fill(255);
        rect(b*10, height - arr[b], 9, arr[b]);
    }
  }
