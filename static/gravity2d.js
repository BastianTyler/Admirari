let balls = [] // List to store multiple ball objects

function setup() {
  canvas = createCanvas(400, 400)
  angleMode(DEGREES)

  // Create multiple ball objects
  for (let i = 0; i < 5; i++) {
    balls.push(
      new object(
        random(width),
        random(height),
        random(-3, 3),
        random(-3, 3),
        10
      )
    )
  }
}

function draw() {
  background(220)

  for (let ball of balls) {
    ball.accelerate(1, 1)
    ball.updatePos()
    ball.checkBounds()
    ball.checkCollision()
    ball.display()
  }
}

class object {
  constructor(x, y, vx, vy, r) {
    this.position = createVector(x, y)
    this.velocity = createVector(vx, vy)
    this.radius = r
    this.color = color(random(255), random(255), random(255))
  }

  accelerate(x, y) {
    this.velocity.x += x
    this.velocity.y += y
  }

  updatePos() {
    this.position.x += this.velocity.x
    this.position.y += this.velocity.y
  }

  display() {
    fill(this.color)
    ellipse(this.position.x, this.position.y, this.radius * 2)
  }

  checkBounds() {
    this.position.x = max(
      this.radius,
      min(width - this.radius, this.position.x)
    )
    this.position.y = max(
      this.radius,
      min(height - this.radius, this.position.y)
    )

    if (
      this.position.x === this.radius ||
      this.position.x === width - this.radius
    ) {
      this.velocity.x *= -0.85
    }
    if (
      this.position.y === this.radius ||
      this.position.y === height - this.radius
    ) {
      this.velocity.y *= -0.85
    }
  }

  checkCollision(object) {
    let combinedRadius = this.radius + object.radius
    let distance = dist(this.x, this.y, object.x, object.y)

    if (distance <= combinedRadius) {
      this.velocity *= -1
      object.velocity *= -1
    }
  }
}
