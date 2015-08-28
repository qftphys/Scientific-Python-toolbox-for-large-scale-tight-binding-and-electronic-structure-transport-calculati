"""
Sile object for reading/writing CUBE files
"""

from __future__ import print_function

import numpy as np

# Import sile objects
from sids.io.sile import *

# Import the geometry object
from sids import Geometry, Atom, SuperCell, Grid

__all__ = ['CUBESile']


_zero = np.zeros([3],np.float64)
_one = np.ones([3],np.float64)

class CUBESile(Sile):
    """ CUBE file object """
    # These are the comments
    _comment = []

    def write_geom(self,geom,size=_one,fmt='15.10e',origo=_zero,*args,**kwargs):
        """ Writes the `Geometry` object attached to this grid """
        sile_raise_write(self)

        if not hasattr(self,'fh'):
            # The file-handle has not been opened
            with self:
                return self.write_geom(geom,size,fmt,origo,*args,**kwargs)

        _fmt = '{:d} {:15.10e} {:15.10e} {:15.10e}\n'

        # Add #-of atoms and origo
        self._write(_fmt.format(len(geom),*origo/geom.Length))

        # Write the cell and voxels
        dcell = np.empty([3,3],np.float64)
        for ix in range(3):
            dcell[ix,:] = geom.cell[ix,:] / size[ix] / geom.Length
        self._write(_fmt.format(size[0],*dcell[0,:]))
        self._write(_fmt.format(size[1],*dcell[1,:]))
        self._write(_fmt.format(size[2],*dcell[2,:]))

        tmp = ' {:' + fmt + '}'
        _fmt = '{:d} 0.0' + tmp + tmp + tmp + '\n'
        for ia in geom:
            self._write(_fmt.format(geom.atoms[ia].Z,*geom.xyz[ia,:]/geom.Length))


    def write_grid(self,grid,fmt='%.5e',*args,**kwargs):
        """ Writes the geometry to the contained file """
        # Check that we can write to the file
        sile_raise_write(self)

        if not hasattr(self,'fh'):
            # The file-handle has not been opened
            with self:
                return self.write_grid(grid,fmt)

        # Write header
        self._write('\n')
        self._write('sids --- CUBE file\n')

        # Write the geometry
        self.write_geom(grid.geom,size=grid.grid.shape,*args,**kwargs)

        g_size = np.copy(grid.grid.shape)

        grid.grid.shape = (-1,)

        # Write the grid
        np.savetxt(self.fh,grid.grid[:],fmt)

        grid.grid.shape = g_size
        return
        # Write the actual grid
        for ix in range(g_size[0]):
            for iy in range(g_size[1]):
                np.savetxt(self.fh,grid.grid[ix,iy,:],fmt)
                

    def read_sc(self,na=False):
        """ Returns `SuperCell` object from the CUBE file 

        If `na=True` it will return a tuple (na,SuperCell)
        """
        if not hasattr(self,'fh'):
            # The file-handle has not been opened
            with self:
                return self.read_sc()

        self.readline() # header 1
        self.readline() # header 2
        tmp = self.readline().split() # origo
        na = int(tmp[0])
        
        cell = np.empty([3,3],np.float64)
        for i in [0,1,2]:
            tmp = self.readline().split()
            s = int(tmp[0])
            for j in [0,1,2]:
                cell[i,j] = float(tmp[j+1]) * s

        cell = cell * SuperCell.Length
        if na:
            return na, SuperCell(cell)
        return SuperCell(cell)


    def read_geom(self):
        """ Returns `Geometry` object from the CUBE file """
        if not hasattr(self,'fh'):
            # The file-handle has not been opened
            with self:
                return self.read_geom()

        na, sc = self.read_sc(na=True)

        # Start reading the geometry
        xyz = np.empty([na,3],np.float64)
        atoms = []
        for ia in range(na):
            tmp = self.readline().split()
            atoms.append(Atom[int(tmp[0])])
            xyz[ia,0] = float(tmp[1])
            xyz[ia,1] = float(tmp[2])
            xyz[ia,2] = float(tmp[3])

        xyz = xyz * Geometry.Length

        return Geometry(xyz,atoms,sc=sc)


    def read_grid(self):
        """ Returns `Grid` object from the CUBE file """
        if not hasattr(self,'fh'):
            # The file-handle has not been opened
            with self:
                return self.read_grid()

        raise NotImplemented('Reading a CUBE file needs to be created accordingly')

if __name__ == "__main__":
    pass