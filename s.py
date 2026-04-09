print("hello world")
from pyswip import Prolog
prolog = Prolog()
prolog.assertz("father(michael,john)")
results = list(prolog.query("father(michael,X)"))
print("Results:", results)

