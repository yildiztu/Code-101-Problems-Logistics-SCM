import nbformat
import sys
import os

for f in sys.argv[1:]:
    if os.path.exists(f):
        nb = nbformat.read(f, as_version=4)
        nb2 = nbformat.normalize(nb)
        nbformat.write(nb2, f)
        print(f"Normalized {f}")
    else:
        print(f"File not found: {f}")
