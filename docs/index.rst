.. sisl documentation master file, created by
   sphinx-quickstart on Wed Dec  2 19:55:34 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


|pypi|_
|conda|_
|zenodo|_
|license|_
|donate|_

|buildstatus|_
|gitter|_
|codecov|_


Welcome to sisl documentation!
==============================

sisl is a tool to manipulate an increasing amount of density functional
theory code input and/or output.
It is also a tight-binding code implementing extremely fast and scalable
tight-binding creation algorithms (`>1,000,000` orbitals).
sisl is developed in particular with `TBtrans`_ in mind to act as a tight-binding
Hamiltonian input engine for *N*-electrode transport calculations.

sisl is hosted here http://github.com/zerothi/sisl.


Features
--------

sisl consists of several distinct features:

* Geometries; create, extend, combine, manipulate different geometries readed from
  a large variety of DFT-codes and/or from generically used file formats.

* Hamiltonian; easily create tight-binding Hamiltonians with user chosen number of
  orbitals per atom. Or read in Hamiltonians from DFT software such as `Siesta`_,
  `Wannier90`_, etc. Secondly, there is intrinsic capability of orthogonal *and*
  non-orthogonal Hamiltonians.

* Generic output files from DFT-software. A set of output files are implemented
  which provides easy examination of output files.

* Command line utilities for processing of data files for a wide
  variety of file formats:

  * :ref:`script_sdata`
    Read and transform *any* sisl data file. 
    This script is capable of handling geometries, grids, special
    data files such as binary files etc.

  * :ref:`script_sgeom` a geometry conversion tool which reads and writes
    many commonly encounted files for geometries, such as XYZ files etc.
    as well as DFT related input and output files.

  * :ref:`script_sgrid` a real-space grid conversion tool which reads and writes
    many commonly encounted files for real-space grids.

  
:ref:`Installation <installation>`
----------------------------------

Follow :ref:`these steps <installation>` to install sisl.


Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. toctree::
   :hidden:
   :maxdepth: 2

   introduction
   other.rst

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Publications

   cite
   publications

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: User Guide
   
   installation
   tutorials.rst
   examples.rst
   scripts/scripts
   rst/files

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Reference documentation
   
   api


.. |buildstatus| image:: https://travis-ci.org/zerothi/sisl.svg
.. _buildstatus: https://travis-ci.org/zerothi/sisl

.. |pypi| image:: https://badge.fury.io/py/sisl.svg
.. _pypi: https://badge.fury.io/py/sisl

.. |license| image:: https://img.shields.io/badge/License-LGPL%20v3-blue.svg
.. _license: https://www.gnu.org/licenses/lgpl-3.0

.. |conda| image:: https://anaconda.org/conda-forge/sisl/badges/installer/conda.svg
.. _conda: https://anaconda.org/conda-forge/sisl

.. |codecov| image:: https://codecov.io/gh/zerothi/sisl/branch/master/graph/badge.svg
.. _codecov: https://codecov.io/gh/zerothi/sisl

.. |donate| image:: https://img.shields.io/badge/Donate-PayPal-green.svg
.. _donate: https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=NGNU2AA3JXX94&lc=DK&item_name=Papior%2dCodes&item_number=codes&currency_code=EUR&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted

.. |zenodo| image:: https://zenodo.org/badge/doi/10.5281/zenodo.597181.svg
.. _zenodo: https://doi.org/10.5281/zenodo.597181

.. |gitter| image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
.. _gitter: https://gitter.im/sisl-tool/Lobby
