(use-modules (ice-9 readline)) (activate-readline)
(use-modules (ice-9 pretty-print))
(add-to-load-path "/usr/local/share/opencog/scm")
(add-to-load-path ".")
(use-modules (opencog))
;(use-modules (opencog query))
(use-modules (opencog exec))



(ConceptNode "HelloWorld")
(InheritanceLink (ConceptNode "Fox") (ConceptNode "Animal"))

(define num1 (NumberNode 3)) 
(define num2 (NumberNode 5))
(define link (PlusLink num1 num2))
; (display (cog-execute! link)) 