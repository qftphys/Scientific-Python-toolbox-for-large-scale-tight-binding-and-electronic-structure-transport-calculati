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

`xsf`
   `XSFSile` file format, XCrySDen_ file format


.. _XCrySDen: http://www.xcrysden.org
