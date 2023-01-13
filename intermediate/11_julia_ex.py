"""
Python Libraries - Julia

https://towardsdatascience.com/how-to-embed-your-julia-code-into-python-to-speed-up-performance-e3ff0a94b6e
https://blog.esciencecenter.nl/how-to-call-julia-code-from-python-8589a56a98f2
"""

from julia import Main

Main.eval('[x^2 for x in 0:4]')