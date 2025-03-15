//initialize stuff you want to have global access
let snake
let apple
let gridSize = 20

function setup() {
  createCanvas(400, 400)
  //make a snake and an apple.
  snake = new Snake()
  apple = new Food()
  //change how fast game operates
  frameRate(10)
}

function draw() {
  background(220)
  // show the snake and move it around, also show the first apple.
  snake.show()
  snake.update()
  apple.show()

  //if snake eats the apple I want to spawn a new apple, add a new pos vector to the snake, despawn old apple. If snake head is on apple box then snake eats apple.
  //I have apple x and apply y, I need head x, and head y,
  if (snake.eat(apple)) {
    snake.body.push(createVector(apple.x, apple.y))
    apple.onEat()
  }
}

function keyPressed() {
  // get keycodes and use those for directions
  if (keyCode === UP_ARROW) snake.setDir(0, -1)
  else if (keyCode === DOWN_ARROW) snake.setDir(0, 1)
  else if (keyCode === RIGHT_ARROW) snake.setDir(1, 0)
  else if (keyCode === LEFT_ARROW) snake.setDir(-1, 0)
}
//Render head rect
//Render apple
//
class Food {
  constructor() {
    this.x = floor(random(floor(width / gridSize))) * gridSize
    this.y = floor(random(floor(height / gridSize))) * gridSize
  }
  show() {
    fill(255, 0, 0)
    rect(this.x, this.y, gridSize, gridSize)
  }
  onEat() {
    this.x = floor(random(floor(width / gridSize))) * gridSize // set x and y to random value and eat and move the apple
    this.y = floor(random(floor(height / gridSize))) * gridSize
    this.show()
  }
}
// make a snake class
class Snake {
  constructor() {
    //Needs a body
    this.body = [createVector(0, 0)] // array of position vectors. Each entry is a segment
    this.vx = 1 // Controls the way it moves
    this.vy = 0
    //Needs a head
    //Needs to move by a square
    //Make it an array of squares
    //Index 0 is the head
  }

  update() {
    let head = this.body[this.body.length - 1].copy() // Copy the frist element
    head.x += this.vx * gridSize // Move it
    head.y += this.vy * gridSize
    this.body.push(head) //Add head to new cell
    this.body.shift() // Remove tail

    //Now we can check if the snake boy hit
    if (this.checkColl()) {
      this.body = [createVector(0, 0)] // array of position vectors. Each entry is a segment
      this.vx = 1 // Controls the way it moves
      this.vy = 0
    }
  }
  setDir(x, y) {
    if (this.body.length > 1 && this.vx == -x && this.vy == -y) return // if we have multiple parts we don't want to let snake boy turn around, otherwise we juse pass in the value from the function getting key inputs
    this.vx = x
    this.vy = y
  }

  eat(apple) {
    let head = this.body[this.body.length - 1].copy() // get a copy of the snake head
    if (head.x == apple.x && head.y == apple.y) {
      // if the apple and head pos match return true and handle the eat
      return true
    }
  }

  //we need a method to check if we hit the edge of the canvas or eat ourselves
  //so we need to check if the head pos matches any body position
  //no idea how to make it optimized, so lets just loop over every body
  //pos and compare it to the head and call it a day

  checkColl() {
    let head = this.body[this.body.length - 1].copy()
    //Boundary check
    if (head.x < 0 || head.x >= width || head.y < 0 || head.y >= height)
      return true
    //Check each body
    for (let i = 0; i < this.body.length - 1; i++) {
      if (head.x == this.body[i].x && head.y == this.body[i].y) return true
    }
    return false
  }
  show() {
    // show the snake
    fill(0, 255, 0)
    for (let segment of this.body) {
      rect(segment.x, segment.y, gridSize, gridSize)
    }
  }
}
