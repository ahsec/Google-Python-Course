#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg
HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US;
rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def get_hostname(filename):
  # Returns the hostname from a file with the following naming convention
  # "animal_code.google.com" "place_code.google.com" where the hostname is code.google.com
  match = re.search(r'([\w+])(_)([\w+.]+)', filename)
  return match.group(3)

def get_path(filename):
  '''
  Reads the content of a log file and returns the path where a puzzle
  image can be found
  10.254.254.28 - - [06/Aug/2007:00:13:47 -0700]
  "GET /edu/languages/google-python-class/images/puzzle/a-baaj.jpg HTTP/1.0"
  302 414 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com,
  foo123@google.com,foo123@google.com,foo123@google.com)"
  Returns /edu/languages/google-python-class/images/puzzle/a-baaj.jpg
  if found, else returns "0"
  '''
  filed = open(filename, 'rU')
  string = filed.read()
  match = re.findall(r'([\w.\s\[\/:\]-]+)("GET\s)([/\w.-]+)', string)
  if match:
    return match
  else:
    return 0

def get_name_tail(url_list):
  # Auxiliary function for the read_urls sorted method.
  # It returns the last word when a filename is named
  # like word-word-word.jpg
  # i.e. For p-bjjc-bbjd.jpg, returns bbjd
  filename_list = []
  print "To match: " + url_list
  match = re.search(r'([\w:/.-])+([\w-]+)-([\w]+)-([\w]+)(.jpg)', url_list)
  filename_list.append(match.group(4))
  return filename_list

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing ordert."""
  hostname = get_hostname(filename)
  paths_list = get_path(filename)
  paths_list2 = []
  paths_list2_sorted = []
  for tuple in paths_list:
    to_check = "http://" + hostname + tuple[2]
    if to_check in paths_list2:
      print "Duplicate found: " + to_check
    elif "puzzle" in tuple[2]:
      paths_list2.append(to_check)
  # Special sort method if the filename is formed like: p-bjjc-bbjd.jpg
  url = paths_list2[0]
  match = re.search(r'([\w:/.-])+([\w-]+)-([\w]+)-([\w]+)(.jpg)', url)
  if match:
    print "Special naming detected"
    paths_list2 = sorted(paths_list2, key = get_name_tail)
  else:
    paths_list2.sort()
  return paths_list2

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # If destination directory doesn't exist it will be created
#  check = os.listdir(dest_dir)
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir, mode = 511)
  index = 0
  # Creates file index.html
  file_index = open(dest_dir + '/index.html', 'w')
  index_string = """ <verbatim>
<html>
<body>"""
  file_index.write(index_string)
  for url in img_urls:
    ufile = urllib.urlopen(url)
    info = ufile.info()
    print "Downloaded: " + url
    text = ufile.read()
    file_dest = open(dest_dir + '/img' + str(index) + ".jpg", 'w')
    file_dest.write(text)
    file_index.write('<img src="img' + str(index) + '.jpg">')
    file_dest.close()
    index = index + 1
  index_string = """</body>
</html>"""
  file_index.write(index_string)
  file_index.close()

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
