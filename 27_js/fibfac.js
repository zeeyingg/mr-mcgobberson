// Josh's Joltin' Giants
// SoftDev pd08
// K27 -- Basic functions in JavaScript
// 2023-04-03t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.


function fact(a) {
    if(a <= 1){
        return 1
    } else{
        return fact(a - 1) * a
    }
}

function fib(a){
    if( a <= 1){
        return a 
    } else {
        return (fib(a - 1) + fib(a - 2))
    }
 }