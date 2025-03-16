let arr = [];
let i = 0;
let p 
let barSize = 4



function setup(){
  createCanvas(600,400);
  for(let i = 0; i < width/barSize; i++){
    arr.push(random(height))
  }
  frameRate(10)
}
function draw(){
    background(10);

    if(i < arr.length){
        let minIndex = i;
        let min = arr[i];
        for(j = i+1; j < arr.length; j++){
            if(arr[j] < min){
                minIndex = j;
                min = arr[j];
            }
        }
        let temp = arr[minIndex]
        arr[minIndex] = arr[i];
        arr[i] = temp;
      i++;
    }
    
    for(let b = 0; b < arr.length; b++){
        if(b == i){
          fill(255, 0, 0)
        }else fill(255);
        rect(b*4, height - arr[b], 4, arr[b]);
    }
  }