.. include:: links.rst

File formats
============

`sisl` implements a generic interface for interacting with many different file
formats. When using the :doc:`command line utilities<scripts>` all these files
are accepted as input for, especially :ref:`script_sdata` while only those which
contains geometries (:py:class:`Geometry`) may be used with :ref:`script_sgeom`.

In `sisl` any file is named a `Sile` to destinguish it from `File`.

Here is a list of the currently supported file-formats with the file-endings
defining the file format:

`xyz`
   `XYZSile` file format, generic file format for many geometry viewers.

`cube`
   `CUBESile` file format, real-space grid file format (also contains geometry)

`xsf`
   `XSFSile` file format, XCrySDen_ file format

`ham`
   `HamiltonianSile` file format, native file format for `sisl`

`dat`
   `TableSile` for tabular data

Below there is a list of file formats especially targetting a variety of DFT codes.

* BigDFT_
  File formats inherent to BigDFT_:

  `ascii`
      `ASCIISileBigDFT` input file for BigDFT_, currently only implements geometry

* SIESTA_
  File formats inherent to SIESTA_:

  `fdf`
      `fdfSileSiesta` input file for SIESTA_

  `bands`
      `bandsSileSiesta` contains the band-structure output of SIESTA_, with :ref:`script_sdata` one may plot this file using the command-line.

  `out`
      `outSileSiesta` output file of SIESTA_, currently this may be used to
      query certain elements from the output, such as the final geometry, etc.

  `grid.nc`
      `gridncSileSiesta` real-space grid files of SIESTA_. This `Sile` allows
      reading the NetCDF_ output of SIESTA_ for the real-space quantities, such
      as, electrostatic potential, charge density, etc.

  `nc`
      `ncSileSiesta` generic output file of SIESTA_ (only `>=4.1`).
      This `Sile` may contain *all* real-space grids, Hamiltonians, density matrices, etc.
  
  `TSHS`
      `TSHSSileSiesta` contains the Hamiltonian and overlap matrix from a TranSIESTA_ run.

  `TBT.nc`
      `tbtncSileSiesta` is the output file of TBtrans_ which contains all transport
      related quantities.

  `TBT.AV.nc`
      `tbtavncSileSiesta` is the **k**-averaged equivalent of `tbtncSileSiesta`,
      this may be generated using `sdata siesta.TBT.nc --tbt-av<script_sdata>`.

  `XV`
      `XVSileSiesta` is the currently runned geometry in SIESTA_.
