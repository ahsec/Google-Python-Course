#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def get_year(filename):
  """
  This function will extract the year from a file when it is preceded
  by the "<h3 align="center">)(Popularity in )" string
  Open the file with read permissions, search for the corresponding pattern
  and read the 3rd group (the one that contains the year)
  If there's a match will print the year, else it will print an error message
  """
  f = open(filename, 'r')
  year = re.search(r'(<h3 align="center">)(Popularity in )(\d\d\d\d)', f.read())
  if year:
    return year.group(3)
  else:
    print 'File doesn contain the string "Popularity in YEAR". \n Try a different file'
    return(0)

def get_Keys(dictionary):
  """
  Helper function for the sorted function used in the get_name_rank function
  returns the first element of a tuple
  """
  return dictionary[0]

def get_name_rank(filename):
  """
  Reads names and ranks from a file. Name must be preceded by:
  <tr align="right"><td> YEAR </td><td> NAME </td><td> NAME
  Stores matches in "match" variable and creates dictionary.
  Male and female names serve as keys and the rank as value
  returns dictionary sorted by keys (name alphabetically sorted).
  """
  dictionary = {}
  f = open(filename, 'r')
  match = re.findall(r'(<tr align="right"><td>)(\d+)(</td><td>)(\w+)(</td><td>)(\w+)(</td>)', f.read())
  for data in match:
    rank = data[1]
    name_m = data[3]
    name_f = data[5]
    dictionary[name_m] = rank
    dictionary[name_f] = rank
  f.close()
  dictionary_sorted = sorted(dictionary.items(), key = get_Keys)
  return dictionary_sorted

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  ret_list = []
  year = get_year(filename)
  dictionary = get_name_rank(filename)
  ret_list.append(year)
  for tuples in dictionary:
    ret_list.append(tuples[0] + ' ' + tuples[1])
  return ret_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)


  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
#    del args[0]
    string = extract_names(args[1])
    f = open('output.txt', 'w')
    f.write(str(string))
    f.close()

  # This is temporary code to test the 'incermental' milestones, I will call each function from here
  else:
    print extract_names(args[0])

if __name__ == '__main__':
  main()
