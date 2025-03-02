function setup() {
    let canvas = createCanvas(400, 400, WEBGL)
    angleMode(DEGREES)
    canvas.parent('p5-container');
}

function resetBackground(count){
    if (count >= 200)
        count = 0;
}
var count = 0

function draw(){

background(abs(sin(frameCount * 0.1)) * 120)

rotateX(frameCount/10)
noFill()
stroke(255)

for(var i = 0; i < 50; i++){

    var r = map(sin(frameCount), -1,0,0,255)
    var g = map(i, 0, 5, 0, 255)
    var b = map(cos(frameCount), -1, 0, 255, 0)

    stroke(r,g,b)
    rotate(frameCount/12)

    beginShape()
    for(var j = 0; j < 360; j+= 180){

        var rad = i * 5
        var x = -rad * cos(j)
        var y = rad * sin(j)
        var z = sin(frameCount*2 + i * 12) * 50

        vertex(x, y, z)
    }
    endShape(CLOSE)
}
}
