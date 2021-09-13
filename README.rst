====================
Cajun Name Generator
====================


.. image:: https://img.shields.io/pypi/v/cajun_name_generator.svg
        :target: https://pypi.python.org/pypi/cajun_name_generator

.. image:: https://img.shields.io/travis/adammelancon/cajun_name_generator.svg
        :target: https://travis-ci.com/adammelancon/cajun_name_generator

.. image:: https://readthedocs.org/projects/cajun_name_generator/badge/?version=latest
        :target: https://cajun_name_generator.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status



Package to generate random Cajun first and last names.


* Free software: MIT license
* Documentation: https://cajun_name_generator.readthedocs.io.


Example
-------- 
::

    from cajun_name_generator import Cajunnames

    name = Cajunnames()

    
    name.random_first_name(3)    # Prints and returns 3 first names in a list.
    
    name.random_last_name(3)    # Prints and returns 3 last names in a list.
    
    name.random_full_name(3)    # Prints and returns 3 full names in a list.
 



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
