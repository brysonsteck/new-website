#!/usr/bin/python3
# stolen from https://stackoverflow.com/questions/12332975/installing-python-module-within-code

import os
import subprocess
import sys
import shutil

def install(package):
  subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])

if __name__ == "__main__":
  print("Installing dependencies...")
  install('Pillow')
  install('python-dotenv')
  install('django')
  install("fontawesomefree")
  install("django-markdownfield")
  shutil.copy(".env.example", ".env")
  input("\n\nIMPORTANT\nDon't forget to change the secret key environment variable inside the newly created .env file if you are planning on using this during production. Press [ENTER] to continue the migration with the key that is already in the .env.example file. \n")
  print("Migrating database...")
  subprocess.check_call([sys.executable, "manage.py", "migrate"])
