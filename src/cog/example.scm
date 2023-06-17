(use-modules (opencog))

;; Create atoms
(define atom1 (ConceptNode "atom1"))
(define atom2 (ConceptNode "atom2"))

;; Assert an assertion
(assert! (EvaluationLink
           (PredicateNode "is-a")
           atom1
           atom2))

;; Query the Atomspace
(define query (AndLink
               (EvaluationLink
                (PredicateNode "is-a")
                atom1
                atom2)))

(define result (cog-execute! (ConceptNode "query") query))
(display result)

;; Retract an assertion
(retract! (EvaluationLink
           (PredicateNode "is-a")
           atom1
           atom2))





(ConceptNode "HelloWorld")
(InheritanceLink (ConceptNode "Fox") (ConceptNode "Animal"))

(define num1 (NumberNode 3)) 
(define num2 (NumberNode 5))
(define link (PlusLink num1 num2))
; (display (cog-execute! link)) 