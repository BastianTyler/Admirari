let waveSpeed = 2;
let disturbance;
let numDisturbances = 5;
let lineX;
let lineY1, lineY2;
let spacing;
let maxSpacing;
let target = 0;
let secondaryWave;

let linesArray = [];

function setup(){
    createCanvas(400,400);

    lineX = width / 5;
    lineY1 = height / 2 - 100;
    lineY2 = height / 2 + 100;
    maxSpacing = (lineY2 - lineY1) / (numDisturbances - 1);
    spacing = 0;

}
function drawInitialWaveFront(){
    stroke(255)
    line(lineX, lineY1, lineX, lineY2)
    linesArray.push([lineX, lineY1, lineX, lineY2])
}

function drawDisturbances(value){
    fill(255,0,0);
    noStroke();

    for(let i = 0; i < numDisturbances; i++){
        let dotY = lineY1 + i * maxSpacing;
        disturbance = ellipse(lineX + (maxSpacing*value)/2, dotY, 10);

        noFill();
        stroke(255,255,0);
        ellipse(lineX + (value*maxSpacing)/2, dotY, spacing); //here for spacing
        fill(255,0,0);
        noStroke();
    }
}

function drawNewWaveFront(value){
    stroke(255)
    let newX = lineX + (maxSpacing*value)/2;
    line(lineX + (maxSpacing*value)/2, lineY1, lineX + (maxSpacing*value)/2, lineY2)
    linesArray.push([newX, lineY1, newX, lineY2])
}

function drawWaveFronts(){

    for(let i = 0; i < linesArray.length; i++){
        let lineData = linesArray[i];
        line(lineData[0], lineData[1], lineData[2], lineData[3]);
    }
}

function draw(){
   background(30)

    spacing = min(spacing + waveSpeed * 0.5, maxSpacing);
    
    drawInitialWaveFront();
    drawDisturbances(target);
    drawNewWaveFront(target);


     if(spacing >= maxSpacing){
        target ++
        spacing = 0;
     }

     drawWaveFronts();
    
}
