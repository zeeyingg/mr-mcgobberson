// Josh's Joltin' Giants
// SoftDev pd08
// K27 -- Basic functions in JavaScript
// 2023-04-03t
// --------------------------------------------------

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