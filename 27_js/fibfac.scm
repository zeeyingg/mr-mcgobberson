;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname fibfac) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Josh's Joltin' Giants
;SoftDev pd08
;K27 -- Basic functions in JavaScript
;2023-04-03t

;Scheme Antecedents for JS work

;factorial:
(define
fact (lambda (n)
  ( if (< n 2)
       1
       (* n (fact (- n 1))
       ))))
"Factorial"
(fact 1) "...should be  1"
(fact 2) "...should be  2"
(fact 3) "...should be  6"
(fact 4) "...should be  24"
(fact 5) "...should be  120"


;fib:
(define fib (lambda (n)
      ( if (< n 2)
           n
           ( + (fib (- n 1)) (fib (- n 2)) )
           )))


(fib 0) "...should be  0"
(fib 1) "...should be  1"
(fib 2) "...should be  1"
(fib 3) "...should be  2"
(fib 4) "...should be  3"
;=================================================================

