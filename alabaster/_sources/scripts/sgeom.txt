
`sgeom`
=======

The :program:`sgeom` executable is a tool for reading and transforming general
coordinate formats to other formats, or alter them.

For a short help description of the possible uses do:

::
    sgeom --help


Here we list a few of the most frequent used commands.


Conversion
----------

The simplest usage is transforming from one format to another format.
``sgeom`` takes at least two mandatory arguments, the first being the
input file format, and the second (and any third + argumets) the output
file formats

::
   sgeom <in> <out> [<out2>] [[<out3>] ...]

Hence to convert from an ***fdf*** SIESTA input file to an ***xyz*** file
for plotting in a GUI program one can do this:

::
    sgeom RUN.fdf RUN.xyz

and the ``RUN.xyz`` file will be created.
    
Available formats
^^^^^^^^^^^^^^^^^

The currently available formats are:

 - ***xyz***, standard coordinate format
 Note that the the *xyz* file format does not *per see* contain the cell size.
 The `XYZSile` writes the cell information in the ``xyz`` file comment section (2nd line). Hence if the file was written with sids you retain the cell information.
 - ***gout***, reads geometries from GULP output
 - ***nc***, reads/writes NetCDF4 files created by SIESTA
 - ***TBT.nc***/***PHT.nc***, reads NetCDF4 files created by TBtrans/PHtrans
 - ***tb***, intrinsic file format for geometry/tight-binding models
 - ***fdf***, SIESTA native format
 - ***XV***, SIESTA coordinate format with velocities
 - ***POSCAR***/***CONTCAR***, VASP coordinate format, does *not* contain species, i.e. returns Hydrogen geometry.
 - ***ASCII***, BigDFT coordinate format


Advanced Features
-----------------

More advanced features can be represented here.

Repeating/Tiling structures
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Often one wishes to expand a structure an integer number of times along
certain cell directions. This is useful for creating larger bulk structures.
To repeat a structure do

::
    sgeom --repeat [ax|yb|zc] <int> <in> <out>

which repeats the structure one atom at a time, ``<int>`` times, in the corresponding direction.
Note that ``x`` and ``a`` correspond to the same cell direction.

To repeat the structure in *chunks* one can use the ``tiling``:

::
    sgeom --tile [ax|yb|zc] <int> <in> <out>

which results in the same structure as ``--repeat`` however with different atomic ordering.

Both tiling and repeating have the variants:

::
    sgeom -t[xyz] <int> -r[xyz] <int>

for shorthand commands.

To repeat a structure 4 times along the *x* cell direction:

::
   sgeom --repeat x 4 RUN.fdf RUN4x.fdf
   sgeom --repeat-x 4 RUN.fdf RUN4x.fdf
   sgeom --tile x 4 RUN.fdf RUN4x.fdf
   sgeom --tile-x 4 RUN.fdf RUN4x.fdf

where all the above yields the same structure.
   
Rotating structure
^^^^^^^^^^^^^^^^^^

To rotate the structure around certain cell directions one can do:

::
    sgeom --rotate [ax|yb|zc] <angle> <in> <out>

which rotates the structure around the origo with a normal vector along the
specified cell direction. The input angle is in degrees and *not* in radians.

Again there are shorthand commands:

::
    sgeom -R[xyz] <angle>


