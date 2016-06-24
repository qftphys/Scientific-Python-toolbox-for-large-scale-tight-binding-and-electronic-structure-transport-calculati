.. highlight:: python

.. sisl documentation master file, created by
   sphinx-quickstart on Wed Dec  2 19:55:34 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to sisl documentation!
==============================

This documentation has been created from version: |release|.

sisl is a tool to easily create geometries and handle input/output files
from various DFT codes. Although this is based on the SIESTA/TranSIESTA
DFT code it is far from limited to deal with *only* this code. 

A list of key components are

:ref:`scripts_sgeom`
   Read and transform generic coordinate files from
   one format into other formats.

:ref:`scripts_sgrid`
   Read and transform *grid* data, such as electronic
   densities, electrostatic potentials etc. and save them in various
   formats.

Script based handling via Python classes and objects that handles 

  * Atomic species
  * Unit cells (using a super cell approach)
  * Geometries, with associated atomic species and unit cells
  * Grids, with associated unit cells
  * Tight-binding models using a sparse data structure for easy
    creation and calculation of eigenvalues

Installation
============

The easiest way to install ``sisl`` is via the :program:`pypi` interface.
Install via:

.. code-block:: bash

   pip install sisl

Alternatively you can download the releases on the
`release page <gh-releases_>`_. And install via the regular :program:`setup.py`
interface:

.. code-block:: bash

   python setup.py install

which will install ``sisl`` in your default location, use :program:`--prefix <path>` for
manual control of the placement.

Requirements
------------

To succesfully use ``sisl`` these Python packages must be installed:

 - `numpy`_
 - `scipy`_ 
 - `netcdf4-python`_

Contents:

.. toctree::
   :maxdepth: 3

   scripts/sgeom
   scripts/sgrid
	      
.. autosummary::
   :toctree: _autosummary


The API documentation of the ``sisl`` package can be found `here <sisl>`.

      
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Documentation in other themes
=============================

The ``sisl`` documentation has been created with several different themes
of documentation.
This is mainly of convenience until I have figured out which one is the
best suited theme for this documentation.

If you have any preferences please let me know.

* `Alabaster`_ theme (good)
* `Agogo`_ theme (good)
* `Bizstyle`_ theme (default, good)
* `Classic`_ theme (ok)
* `Scrolls`_ theme (good)
* `Sphinx RTD`_ theme (ok)


.. _Alabaster: ../alabaster/index.html
.. _Agogo: ../agogo/index.html
.. _Bizstyle: ../bizstyle/index.html
.. _Classic: ../classic/index.html
.. _Scrolls: ../scrolls/index.html
.. _Sphinx RTD: ../sphinx_rtd_theme/index.html
.. _gh-releases: http://github.com/zerothi/sisl/releases
.. _pypi-releases: http://pypi.python.org/pypi/sisl/

.. These are external links:
.. _netcdf4-python: http://github.com/Unidata/netcdf4-python
.. _numpy: http://github.com/numpy/numpy
.. _scipy: http://github.com/scipy/scipy

