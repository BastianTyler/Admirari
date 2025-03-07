let angleX = 0;
let angleY = 0;

function setup() {
  canvas = createCanvas(600, 600, WEBGL);
  angleMode(degrees)
  canvas.parent('p5-container');
  
}

function draw() {
  
  background(112,122,213);

  scale(1, -1);
  translate(0, -100);

  // Calculate coordinates.
  let x = frameCount;
  let y = 15 * log(x);

  // Draw a point.
  sphere(x, y, 0);

  rotateX(angleX);
  rotateY(angleY);
  drawAxes();
  drawGridXY();

  
}

function drawMatrixPlane() {
  push(); // Save transformation state

  // Define transformation matrix for the plane
  let a = 1, b = 0, c = 0, d = 0; // Row 1
  let e = 0, f = 2, g = 1, h = 0; // Row 2
  let i = 0, j = 1, k = 0, l = 0; // Row 3
  let m = 0, n = 0, o = 0, p = 1; // Row 4 (Translation at the end)

  applyMatrix(a, b, c, d,  // First column
              e, f, g, h,  // Second column
              i, j, k, l,  // Third column
              m, n, o, p); // Fourth column (Translation)

  fill(100, 100, 255, 100);
  noStroke();
  plane(200, 200); // Draw a plane at the transformed position

  pop(); // Restore transformation state
}


// Draw X, Y, Z axes
function drawAxes() {
  strokeWeight(2);

  // X-axis (Red)
  stroke(255, 0, 0);
  line(-200, 0, 0, 200, 0, 0);

  // Y-axis (Green)
  stroke(0, 255, 0);
  line(0, -200, 0, 0, 200, 0);

  // Z-axis (Blue)
  stroke(0, 0, 255);
  line(0, 0, -200, 0, 0, 200);
}

  

  // Draw grid lines in the XY plane
function drawGridXY() {
    stroke(150);
    strokeWeight(0.5);
    for (let i = -200; i <= 200; i += 20) {
      line(i, -200, 0, i, 200, 0); // Vertical grid lines
      line(-200, i, 0, 200, i, 0); // Horizontal grid lines
    }
  }


  // Handle mouse drag for rotation for p5
function mouseDragged() {
  let sensitivity = 0.01;
  angleY += (mouseX - pmouseX) * sensitivity;
  angleX += (mouseY - pmouseY) * sensitivity;
}