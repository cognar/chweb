#!flask/bin/python
import os
import sys

sys.path.append('/home/apps/chweb/')

from flipflop import WSGIServer
from app import app as application

if __name__ == '__main__':
	WSGIServer(app).run()
