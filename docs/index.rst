.. Cajun Name Generator documentation master file, created by
   sphinx-quickstart on Tue Sep  7 16:57:38 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Cajun Name Generator's documentation!
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Example
--------
::
from cajun_name_generator import Cajunnames

cng = Cajunnames()

# Prints and returns 3 first names in a list.
cng.random_first_name(3)
# Prints and returns 3 last names in a list.
cng.random_last_name(3)
# Prints and returns 3 full names in a list.
cng.random_full_name(3)


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
