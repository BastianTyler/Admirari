// Handle mouse drag for rotation for p5
function mouseDragged() {
    let sensitivity = 0.01;
    angleY += (mouseX - pmouseX) * sensitivity;
    angleX += (mouseY - pmouseY) * sensitivity;
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


    // Draw X, Y, Z axes
function drawAxes(size) {
    strokeWeight(2);
  
    // X-axis (Red)
    stroke(255, 0, 0);
    line(-size, 0, 0, size, 0, 0);
  
    // Y-axis (Green)
    stroke(0, 255, 0);
    line(0, -size, 0, 0, size, 0);
  
    // Z-axis (Blue)
    stroke(0, 0, 255);
    line(0, 0, -size, 0, 0, size);
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

  function drawGridXY(size, increment) {
    stroke(150);
    strokeWeight(0.5);
    for (let i = -size; i <= size; i += size/increment) {
      line(i, -size, 0, i, size, 0); // Vertical grid lines
      line(-size, i, 0, size, i, 0); // Horizontal grid lines
    }
  }

  // Use a transformation matrix to position the plane
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
//Flip the velocity
  function flipVel() {
    if (pos.x >= width - 10 || pos.x <= 0) { // Account for rectangle's width
      vel.x *= -1; // Reverse velocity on x-axis
    }
    if (pos.y >= height - 10 || pos.y <= 0) { // Account for rectangle's height
      vel.y *= -1; // Reverse velocity on y-axis
    }
  }
  