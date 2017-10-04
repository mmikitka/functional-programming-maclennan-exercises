(defun fmap (f)
  #'(lambda (S)
    (if (null S) nil
      (cons (funcall f (car S))
            (funcall (fmap f) (cdr S)) )) ))

(format t "~A"
        (funcall (fmap #'(lambda (x) (+ x 1)) ) (list 1 2 3 4)) )

(defun comp (f g)
  #'(lambda (x)
      (funcall f (funcall g x)) ) )

(format t "~A"
        (funcall (comp #'sin #'cos) 0) )

(defun constr (f g)
  #'(lambda (x)
      (list (funcall f x) (funcall g x)) ))

(format t "~A"
        (funcall (constr #'sin #'cos) 0) )

(defun dprod (f g)
  #'(lambda (x y)
      (list (funcall f x) (funcall g y)) ))

(format t "~A"
        (funcall (dprod #'sin #'cos) 0 0) )
