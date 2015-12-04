
#
# Small module to read in the needed information
#

import os.path

# Get this file's directory
d = os.path.dirname(__file__)

with open(os.path.sep.join([d,'..','doc.tag'])) as fh:
    v = fh.readline()

try:
    # Read in the theme applied
    with open(os.path.sep.join([d,'..','html.theme'])) as fh:
        html_theme = fh.readline().replace('\n','')
except:
    # Have a default
    html_theme = 'sphinx_rtd_theme'

try:
    version = '.'.join(v.split('.')[:2])
except:
    version = v
release = v

# Clean up
del d, v
        
