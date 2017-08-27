iversions
^^^^^^^^^

A cell magic command for IPython/Jupyter to display name and version of
all imported (non built-in) modules in the current session.

Installation
^^^^^^^^^^^^

.. code:: bash

    $ pip install iversions

Usage
^^^^^

.. code:: python

    In [1]: %load_ext iversions

    In [2]: import numpy as np
       ...: import pandas as pd
       ...: import tensorflow as tf
       ...: import os
       ...: import sys

    In [3]: %iversions
    numpy       1.13.1
    pandas      0.20.3
    tensorflow  1.3.0

    Python 3.6.2 [Sun Aug 27, 2017 13:50:43]

    In [4]:



Inspired by amazing similar projects:
=====================================

-  `version\_information <https://github.com/jrjohansson/version_information>`__
-  `watermark <https://github.com/rasbt/watermark>`__


TODO
====

- Add a feature to output to ``requirements.txt``


KNOWN ISSUES
============

- Non-module imports do not work e.g. ``from X import Y``
