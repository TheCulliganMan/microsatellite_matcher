#!/usr/bin/env python
import sys

import microsatellite_matcher as mm

if len(sys.argv) > 1:
    mm.main()
else:
    print("Please specify a filename")
