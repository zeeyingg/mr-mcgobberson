// Team Josh's Joltin Giants :: Ziying, Joshua
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-17
// --------------------------------------------------

console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var 
// ** CAN be run in the dev console ex: f(3) = 33
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist"); // this refers to the html <ol id="thelist">
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem); // adds an 'item'(the input text) to the list
};


var removeItem = function(n) { // removes item by index on the ol
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() { // adds the red clsss to all <li>, Does not change the already colored items to red
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red'); 
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

var fib = (a) => {
  if(a == 0 || a == 1){
    return a
  }
  var count = 2
  var kot1 = 1
  var kot2 = 1
  var kot3 = 1

  while(count < a){
      var temp = kot3
      kot3 = kot3 + kot2
      kot1 = kot2
      kot2 = temp
      count++
  }
  return kot3;
};

var fac = (a) => {
  if(a <= 1){
    return 1
  } else{
      return fac(a - 1) * a
  }
};

var gcd = (a, b) => {
  if(a < b){
    c = a;
  }else{
    c = b;
  }
  while (!(a % c == 0 && b % c == 0)){
    if(c > a && c > b){
      return 1;
    }
    c--;
  }
  return c;
};

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  var retVal = param1;
  return retVal;
};


console.log(addItem("Fibbonaci calculation of 10 is " + fib(10)));
console.log(addItem("Factorial calculation of 10 is " + fac(10)));
console.log(addItem("GCD calculation of 60 and 48 is " + gcd(60, 48)));



