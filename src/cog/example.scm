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