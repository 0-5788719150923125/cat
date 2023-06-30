(include "/app/src/cog/common.scm")



(define atom (ConceptNode (list-ref args 0)))

(define atom-name (name-string atom))

(display atom-name)
