.. sids documentation master file, created by
   sphinx-quickstart on Wed Dec  2 19:55:34 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to sids's |release| documentation!
==========================================

sids is a tool to easily create geometries and handle input/output files
from various DFT codes. Although this is based on the SIESTA/TranSIESTA
DFT code it is far from limited to deal with *only* this code. 

A list of key components are

:program:`sgeom`
   Read and transform generic coordinate files from
   one format into several others.

:program:`sgrid`
   Read and transform *grid* data, such as electronic
   densities, electrostatic potentials etc. and save them in various
   formats.

Script based handling via Python classes and objects that handles 

  - Atomic species
  - Unit cells (using a super cell approach)
  - Geometries, with associated atomic species and unit cells
  - Grids, with associated unit cells
  - Tight-binding models using a sparse data structure for easy
    creation and calculation of eigenvalues


Contents:

.. toctree::
   :maxdepth: 3

.. autosummary::
   :toctree: _autosummary


The API documentation of the `sids` package can be found `here <sids>`.

      
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

