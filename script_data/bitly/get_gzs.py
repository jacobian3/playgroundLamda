#!/usr/bin/env python

import pdb
import json
import urllib2
import re

fname = '2011.htm'



links = re.findall(r'<a href="(\/bitly_archive\/usagov_bitly_data(2011-07-08-\d+\.gz))">', open(fname).read())

for link, name in links:
    full_link = "http://1usagov.measuredvoice.com" + link
    response = urllib2.urlopen(full_link).read()
    with open(name, 'wb') as fh:
      fh.write(response)





