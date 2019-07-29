#! /usr/bin/env python2

from pprint import pprint, pformat
import sys
import re
import json

fname = sys.argv[1]

fp = open(fname)

def id_string(x, i):
    x = x.lower()
    x = re.sub('''[ ,.-:'"()?]''', '_', x)
    return x + '_%s' % i


current_section = {
  'objectID': 'frontmatter_0',
  'title': 'Frontmatter',
  'content': '',
  'subheadings': [],
}
sections = []
for i, line in enumerate(fp.readlines()):
    if line.startswith('# '):
        sections.append(current_section)
        title = line[2:].strip()
        current_section = {
          'objectID': id_string(fname, i),
          'title': title,
          'content': '',
          'subheadings': [],
        }
    else:
        current_section['content'] += line
    if line.startswith('## '):
        current_section['subheadings'].append(line[3:].strip())

sections.append(current_section)

print json.dumps(sections, indent=2)


