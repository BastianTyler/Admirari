let r1 = 100; // Radius of first circle
let r2 = 30;  // Radius of second (orbiting) circle
let cx, cy;   // Center of first circle
let nD = 6 //Number of disturbances
let theta = 0;

function setup() {
    let canvas = createCanvas(400,400);
    canvas.parent('p5-container');
    cx = width / 2;
    cy = height / 2;
}

function draw() {
    background(30);
    
    // Draw first circle
    noFill();
    stroke(255);
    ellipse(cx, cy, r1 * 2); // First circle

    for(var i = 0; i <= 6; i++){

        theta = TWO_PI/nD * i //Get angle to place origin of each disturbance

        // Compute second circle's position using polar coordinates
        let x2 = cx + r1 * cos(theta);
        let y2 = cy + r1 * sin(theta);
        
        // Draw second (orbiting) circle
        fill(100, 200, 255);
        noStroke();
        ellipse(x2, y2, r2 * 2);

    }
    

    
    
    
    // Increment theta for animation
    // theta += 0.02; // Adjust speed
}
