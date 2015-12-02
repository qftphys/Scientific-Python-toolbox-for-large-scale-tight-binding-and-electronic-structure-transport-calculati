
#
# Small module to read in the needed information
#

import os.path

# Get this file's directory
d = os.path.dirname(__file__)

with open(os.path.sep.join([d,'..','doc.tag'])) as fh:
    v = fh.readline()

version = '.'.join(v[:2])
release = v

# Clean up
del d, v
        
