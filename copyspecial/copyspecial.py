#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_paths(dir):
  # This function lists all the files in the current directory and
  # prints the path of the files named following the pattern _w_
  # where w is one or more word chars.
  special_files = []
  paths = [] 
  files = os.listdir(dir)
  for names in files:
    match = re.search(r'[\w]*__\w+__[\w]*.\w+', str(names))
    if match:
      special_files.append(match.group())
  for name in special_files:
    paths.append(os.path.abspath(os.path.join(dir, name)))
  return paths
  exit(0)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions

  else:
    get_special_paths(args[0])
  
if __name__ == "__main__":
  main()
