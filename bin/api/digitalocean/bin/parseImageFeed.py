#!/usr/bin/env python
#
# parseImageFeed.py
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
import argparse
import imp
#import logger
import requests

logWrite(message):
	#need logger
	print "parseImageFeed.py: " + str(message)

getImageFeed(apiToken,url,retries):
	pageState=1
	while (pageState == 1) and (retries > 0):
		try:
			#
			# Need to send API_TOKEN header.
			#
			page = requests.get(url)
			pageState = 0
		except Exception as err:
			logWrite "getImageFeed() failed to connect to API."
			logWrite "    ERROR: " + str(err) + "\n"
			pageState = 1	
		retries = retries - 1

	if pageState == 1:
		logWrite "getImageFeed() failed: " + str(err)
		logWrite "cloud vendor API may be down or deployShell cannot"
		logWrite "connect to the internet at this time.\n"
		sys.exit(1)
	# Connection established if pageState == 0
	return page




parseFeedResponse(page):
	logWrite "parseFeedResponse() starting"
	
	logWrite "page.text: " + page.text

	try: 
		json=json.loads(page.text)
	except Exception as err:
		logWrite "parseFeedResponse() failed to parse JSON."
		sys.exit(1)

	#
	# Need to enumerate JSON properties into an array
	# of arrays, where each row describes a single
	# record (image) and each column describes the
	# properties of the aforesaid image-row.
	#

	return json
	logWrite "parseFeedResponse() done."




mapFeedResponse(jsonFeed):
	logWrite "mapFeedResponse() starting."
	map = imp.load_source('module.name', 'mapHandler.py')
	map.MapClass()
	baseMap=map.load('images')
	imageMap=[];
	i=0
	#
	# For every image in baseMap[], 
	# find a matching image in jsonFeed.
	#
	for baseImage in baseMap:
		imageMap.append(
			{ 'name',baseImage['name']
		)
		#
		# Create a dictionary of rows, where each
		# row identifies a single image.
		#
		imageMap[i]=(
						image['name']
			
		
		#
		# Each images should identify a friendly name
		# an imageId and the deployShellImageId.
		#
	return imageMap
	logWrite "mapFeedResponse() done."




writeMapFile(mapData,mapFileName):
	logWrite "writeMapFile(): starting"
	#
	try:
		f=open(mapFileName,'w')
	except:
		logWrite "writeMapFile() failed to open map file."
		sys.exit(1)
	try:
		f.write(mapData)
	#
	logWrite "writeMapFile(): done."	
	
	
	
	
main():
	#
	#	Parse command line arguments.
	#
	#	USAGE:
	#		$0 apiToken mapFileName
	#
	url=https://api.digitalocean.com/v2/sizes
	apiToken=''
	mapFileName=''
	
	parser = argparse.ArgumentParser(
		description='parseImageFeed.py'
	)
	parser.add_argument(
		'apiToken', 
		type=string,
		help='vendor-generated API Token'
	)
	parser.add_argument(
		'mapFileName',
		type='string',
		help='map filename to generate.'
    )
	args = parser.parse_args()
		
	writeMapFile(
		mapFeedResponse(
			parseFeedResponse(
					getImageFeed(apiToken,url,3)
			)
		),mapFileName
	)
	sys.exit(0)


if __name__ == "main":
	main()
else:
	logWrite("parseImageFeed.py must be run directly.")
	sys.exit(1)