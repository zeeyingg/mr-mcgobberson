// Josh's Joltin' Giants
// SoftDev pd08
// K30 -- Getting more comfortable with the dev console and the DOM
// 2023-04-24m

//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (e.target.innerHTML === "rect|circ") {
        e.target.innerHTML = "circle";
        mode = "circ";
    }
    else {
        e.target.innerHTML = "rect|circ";
        mode = "rect";
    }
}

var drawRect = function(e) {
    ctx.fillStyle = "black";
    var mouseX = e.clientX - c.offsetLeft + window.pageXOffset; //gets X-coor of mouse when event is fired and offsets it based on the position of the canvas and the offset of the page(scrolling through the pages)
    var mouseY = e.clientY - c.offsetTop + window.pageYOffset; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillRect(mouseX, mouseY, 10, 10);
}

var drawCircle = function(e){
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "orange";
    ctx.arc(mouseX, mouseY, 10, 0, 2 * Math.PI);
    ctx.fill();
}

// var draw = function(e) {
var draw = (e) => {
    if (mode === "rect") {
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
}

// var wipeCanvas = function() {
var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle") ;
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);


