#!/usr/bin/env python

import json
import os
import pdb
import sys



this_dir = 'gzs'

key_search = sys.argv[1] if len(sys.argv) > 1 else None
key_set = set()

count_lines = 0
error_count = 0

print "timestamp	user_agent	referring_url	short_url_cname	long_url	geo_city_name	country_code	geo_region	accept_language	timezone	lat	long"

for fn in os.listdir(this_dir):
    fp = os.path.join(this_dir, fn)
#    print fp
    fh = open(fp, 'r')
    for line in fh.readlines():
        try:
            td = json.loads(line)
            fields = (td.get('t', ''), td.get('a', ''), td.get('r', ''), td.get('hh', ''), td.get('u', ''), td.get('cy', ''), td.get('c', ''), 
                      td.get('gr', ''), td.get('l', ''), td.get('tz', ''), td.get('ll', ['', ''])[0], td.get('ll', ['', ''])[1])
            fields = [ x if x else '' for x in fields ]
#            print str(fields[0]) + '	' + str(fields[1]) + '	' + str(fields[2]) + '	' + str(fields[3]) + '	' + str(fields[4]) + '	' + str(fields[5]) + '	' + str(fields[6]) + '	' + str(fields[7]) + '	' + str(fields[8])
            print '	'.join([ str(x) for x in fields[0:12] ])
#            print "%s	%s	%s	%s	%s	%s	%s	%s	%s" % (fields)


            """
            for key in ['c', 'hh', 'u', 'hc', 'gr', 'll', 'cy', 'tz', 'hc']:
                if key in td and isinstance(td[key], basestring) and '	' in td[key]:
                    print 'tab value for {}:  {}'.format(key, td[key])
            if key_search:
                if key_search in td:
                    try:
                        if td[key_search] is None:  continue
                        key_set.add(td[key_search])
                    except TypeError:
                        key_set.add(tuple(td[key_search]))
            """
        except ValueError:
            error_count += 1
        count_lines += 1
#    print
    fh.close()

sys.stderr.write('{} total lines'.format(count_lines))
sys.stderr.write('{} total errors'.format(error_count))
if key_search:
    sys.stderr.write('values for {}:  '.format(key_search))
    sys.stderr.write(key_set)


