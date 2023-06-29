(use-modules (ice-9 readline)) (activate-readline)
(use-modules (ice-9 pretty-print))
(add-to-load-path "/usr/local/share/opencog/scm")
(add-to-load-path ".")
(use-modules (opencog))
(use-modules (opencog exec))

; Capture command-line arguments
(define (process-arguments args)
  args)

(define args (cdr (command-line)))