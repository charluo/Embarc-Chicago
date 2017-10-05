#!venv/bin/python

import sys
sys.path.insert(0, './embarc')

from .app import db

print(db.query.all())
