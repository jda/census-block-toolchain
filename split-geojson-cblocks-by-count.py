#!/usr/bin/env python2

import ijson
import argparse
import tempfile
import json
import os
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)

header = """{
"type": "FeatureCollection",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [
"""
footer = "]}"

parser = argparse.ArgumentParser()
parser.add_argument('--out', '-o',
                    default="",
                    help='output files to this dir')
parser.add_argument("geojson")
args = parser.parse_args()

f = open(args.geojson, 'r')
features = ijson.items(f, 'features.item')

county = ""
fout = tempfile.TemporaryFile()

for feature in features:
	fprop = feature['properties']
	cc = fprop["COUNTYFP10"]
	if cc != county:
		if county != "": # footer before closing if not temp
			fout.write(footer)
		fout.close()
		county = cc
		fname = os.path.join(args.out, "cblocks2010-%s.geojson" % (county))
		fout = open(fname, 'w')
		fout.write(header)
	else:
		fout.write(",")
	json.dump(feature, fout, cls=DecimalEncoder)

fout.write(footer)
fout.close()
	#if feature['properties']['COUNTYFP10'] != county:
	#	print "bob"