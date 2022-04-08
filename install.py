#!/usr/bin/python3
# stolen from https://stackoverflow.com/questions/12332975/installing-python-module-within-code

import subprocess
import sys

def install(package):
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
  install('django')
  install("fontawesomefree")
  install("django-markdownfield")