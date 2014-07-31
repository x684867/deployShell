#/usr/bin/env python
#
# mapHandlers.py
#
# The MIT License (MIT)
#
# Copyright (c) 2014 Sam Caldwell.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# This file should load conf/mappings/images.
# and the results should be returned as a comma-delimited
# array of rows, excluding comment(#) rows.
#
import json
import sys

class MapClass:

	def __init__(self,strRoot='~/deployShell'):
		print "MapClass:__init__()"
		self.rootDir=strRoot+'/conf/mappings/'
		

	def load(self,name):
		#
		# Loads map file of given "name" and
		# returns contents in an array of rows.
		#
		print "mapHandlers.load() started"
		fileName=self.rootDir+name
		try:
			f=open(fileName,'r')
		except Exception as err:
			print "mapHandlers.load() failed to open file["+fileName+"]:"+str(err)
			sys.exit(1)
		try:
			mapData=f.read()
		except Exception as err:
			print "mapHandlers.load() failed to read file["+fileName+"]:"+str(err)
			sys.exit(1)

		try:
			return json.loads(mapData)
		except Exception as err:
			print "mapHandlers.load() failed to parse json for ["+fileName+"]:"+str(err)
			sys.exit(1)
		print "mapHandlers.load() done"
	
	def write(self,name,content):
		#
		# Writes content (array of rows) to map named "name."
		#
		fileName=self.rootDir+name
		try:
			f=open(fileName,'w')
		except:
			print "mapHandlers.write() failed to open file ["+fileName+"]:"+str(err)
			sys.exit(1)
		try:
			f.write(json.dumps(content))
		except:
			print "mapHandlers.write() failed to write file ["+fileName+"]:"+str(err)
			sys.exit(1)
		print "mapHandlers.write()"


if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser(
		description="mapHandlers.py (test mode).",
		epilog="This is a unit test mode."
	)
	parser.add_argument('mode', help='mode={load,write}')
	parser.add_argument('mapName', help='Map Name (e.g. images,locations)')
	parser.add_argument('deployShellRoot', help='Base directory where deployShell is found.')
	args = parser.parse_args()

	map=MapClass(args.deployShellRoot)
	print "\n\n--------------------\nTEST RESULTS\n--------------------\n"
	print "TEST(map:"+args.mapName+",root:"+args.deployShellRoot+"):\n"
	if args.mode == "load":	
		print str(map.load(args.mapName))+"\n"
	else:
		print str(map.write(args.mapName,json.loads('{"test":"mapHandlers.py"}')))

	print "\n========================================================\n\n"






