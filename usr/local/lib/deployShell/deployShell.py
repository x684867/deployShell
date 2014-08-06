#!/usr/bin/env python
#
#	deployShell.py
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
# This is the main application file.
#
import getpass
import argparse
from shellRouter import shellRouter
from shellUI import shellUI
from shellMotd import shellMotd
from logger import logger
#
# This file should--
#
#	(1) create commandRouter instance.
#	(2) create shellUI instance
#	(3) create a top-level command-and-control logic and exception handling.
#
#
def main():
	try:
		parser=argparse.ArgumentParser(
			prog="deployShell",
			description="deployShell provides cloud-deployment automation",
			epilog="for more information, see deployshell.com"
		)
		#
		# Reserved for future use to pass in parameters.
		# 	
		parser.add_argument(
			'--logLevel',
			dest='LogLevel',
			default='INFO'
			help='set the logLevel (DEBUG,INFO,WARNING,CRITICAL)'
		)	
		args=parser.parse_args()
		
		logLevel=logger.DEBUG
		if args.logLevel=="INFO":
			logLevel=logger.INFO
		elif args.logLevel=="CRITICAL":
			logLevel=logger.CRITICAL
		elif args.logLevel=="WARNING":
			logLevel=logger.WARNING
		elif args.logLevel=="DEBUG":
			logLevel=logger.DEBUG
		else:
			raise Exception("Invalid logLevel encountered.")
		#
		# Get the current username from the operating system.
		#
		# See http://stackoverflow.com/questions/9323834/python-how-to-get-group-ids-of-one-username-like-id-gn
		# This is a better way.
		#
		user=getpass.getuser()
		#
		errorLog=logger('errors')
		activity=logger('activity')
		#
		# shellMotd should load the message of the day file.
		#
		# motd.welcome() is a short status message for status bars.
		# motd.display() is a longer version of the motd.
		# motd.logout() shows the motd.logout file.
		#
		motd=shellMotd()
		shell=shellUI(motd.welcome(),logLevel=logLevel)
		shell.display(motd.display())
		router=shellRouter(log=logLevel)
		#
		exitShell=False
		while not exitShell:
			try:
				result=command=shell.getCommand()
				if result.error:
					errorLog.write("[user:"+user+"] "+result.message)
				activityLog.write("[user:"+user+"] "+shell.stringify(command))
				result=router.route(command)
				if result.error:
					errorLog.write("[user:"+user+"] "+result.message)
				shell.write(result.message)
			except Exception as err:
				#
				# Handle all non-fatal exceptions here.
				# if we can't handle the exception, then
				# we will raise the exception causing the 
				# shell to terminate.
				#
				raise Exception(str(err))
		#
		# Terminating normal.  Show the log out message of the day.
		#
		motd.logout()
	except Exception as err:
		pass


if __name__ == "__main__":
	main()
	