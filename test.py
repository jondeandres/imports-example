import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import venusian

import imports

scanner = venusian.Scanner()
scanner.scan(imports)

# without previous line, this line fails
from imports.foo import more

print more.less.a
