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
  # This function lists all the files in a directory and
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

def copy_to(paths, dir):
  # copy_to(paths, dir) given a list of paths, copies those files into the given directory
  shutil.copy(paths, dir)

def zip_to(zippath, paths):
  # zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile
  # For a Linux system 
  paths2 = get_special_paths(paths)
  to_send = "zip " + zippath[0]
  for path in paths2:
    to_send = to_send + " " + path
  print "Command I will run: " + to_send
  (status, output) = commands.getstatusoutput(to_send)
  if status: 
    print "Output: " + str(output)
    exit(-1)

def to_dir(dir_dest, dir_orig):
  # If the "--todir dir" option is present at the start of the command line, do not print 
  # anything and instead copy the files to the given directory, creating it if necessary. 
  # Use the python module "shutil" for file copying.
  paths = get_special_paths(dir_orig)
  for filename in paths:
    copy_to(filename, dir_dest)

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
    to_dir(args[1], args[2])
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    zip_to(args[1:-1], args[-1])

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

if __name__ == "__main__":
  main()
