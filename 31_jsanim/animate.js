//getting the stuff from DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = () => {
    ctx.clearRect(0,0,500,500);
};

var radius = 0;
var growing = true;

var grow = function() {
     clear();
    if (growing){
        radius++;
    }   else{
        radius--;
    }

    ctx.beginPath();
    ctx.fillStyle = "blue";
    ctx.arc(250,250,radius,0, 2*Math.PI);
    ctx.fill();
    ctx.stroke();

    if (radius >= 250) growing = false;
    if (radius == 0) growing = true;
    window.cancelAnimationFrame(requestID);
}

var drawDot = () => {
    console.log("asdf");
    console.log(typeof requestID);
    grow();
    requestID = window.requestAnimationFrame(drawDot);
    console.log(radius + "radius is" + "and isGrowing" + growing);
};

var stopIt = function() {
    console.log("stopit");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
