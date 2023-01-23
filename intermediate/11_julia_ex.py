"""
Python Libraries - Julia

https://towardsdatascience.com/how-to-embed-your-julia-code-into-python-to-speed-up-performance-e3ff0a94b6e
https://blog.esciencecenter.nl/how-to-call-julia-code-from-python-8589a56a98f2
"""

from julia import Main
from time import time

t1 = time()
Main.eval("[x^2 for x in 0:1000000]")
t2 = time()

print(t2 - t1)

t1 = time()
c = [x**2 for x in range(1000000)]
t2 = time()

print(t2 - t1)
