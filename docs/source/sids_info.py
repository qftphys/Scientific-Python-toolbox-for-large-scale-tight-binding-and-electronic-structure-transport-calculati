
#
# Small module to read in the needed information
#

import os.path

# Get this file's directory
d = os.path.dirname(__file__)

with open(os.path.sep.join([d,'..','doc.tag'])) as fh:
    v = fh.readline()

try:
    version = '.'.join(v.split('.')[:2])
except:
    version = v
release = v

# Clean up
del d, v
        
