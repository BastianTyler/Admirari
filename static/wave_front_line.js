let waveSpeed = 2;
let disturbance;
let numDisturbances = 15;
let lineX;
let lineY1, lineY2;
let spacing;
let maxSpacing;
let target = 0;
let secondaryWave;
let centerY;
let theta = 45;

let linesArray = [];
let secondaryWaves = [];
let disturbances = [];

function setup(){
    let canvas = createCanvas(400,400);
    canvas.parent('p5-container');
    
    angleMode(DEGREES)
    centerY = height / 3;
    lineX = width / 5 - 50;

    lineY1 = centerY - height / 2 - 100;
    lineY2 = centerY + height / 2 + 100;

    
    
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
        disturbances.push([lineX + (maxSpacing*value)/2, dotY, 10]);

        noFill();
        stroke(255,255,0);
        ellipse(lineX + (value*maxSpacing)/2, dotY, spacing); //here for spacing

        if(spacing >= maxSpacing){
            secondaryWaves.push([lineX + (value*maxSpacing)/2, dotY, spacing]);
         }
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

function drawAllDisturbances(){

    for(let i = 0; i < disturbances.length; i++){

        noFill();
        stroke(255,255,0);

        let disturbanceData = disturbances[i];
        ellipse(disturbanceData[0], disturbanceData[1], disturbanceData[2]);
    }
}

function drawSecondaryWavefronts(){
    noFill();  // Add this line
    stroke(255,255,0);
    for(let i = 0; i < secondaryWaves.length; i++){
        let secondaryWavesData = secondaryWaves[i];
        ellipse(secondaryWavesData[0], secondaryWavesData[1], secondaryWavesData[2]);
    }
}

function draw(){
   background(30)
    
   translate(lineX, centerY);
   rotate(theta)

    spacing = min(spacing + waveSpeed * 0.5, maxSpacing);
    
    drawInitialWaveFront();
    drawDisturbances(target);
    drawNewWaveFront(target);


     if(spacing >= maxSpacing && target <= 7){
        target ++
        spacing = 0;
     }

     drawWaveFronts();
     drawAllDisturbances();
     drawSecondaryWavefronts();
    
}
