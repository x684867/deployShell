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
import argparse
from shellRouter import shellRouter
from shellUI import shellUI
from shellMotd import shellMotd
from shellUser import shellUser
from logger import logger
#
# This file should--
#
#	(1) create commandRouter instance.
#	(2) create shellUI instance
#	(3) create a top-level command-and-control logic and exception handling.
#
#
class deployShell:
	__args=[]
	__logLevel=None
	__activityLog=None
	__errorLog=None
	__user=None
	__shell=None
	__router=None
	
	def __setLogLevel(self):
		self.__logLevel=logger.DEBUG
		if self.__args.logLevel=="INFO":
			self.__logLevel=logger.INFO
		elif self.__args.logLevel=="CRITICAL":
			self.__logLevel=logger.CRITICAL
		elif self.__args.logLevel=="WARNING":
			self.__logLevel=logger.WARNING
		elif self.__args.logLevel=="DEBUG":
			self.__logLevel=logger.DEBUG
		else:
			raise Exception("Invalid logLevel encountered.")
		
			
	def __init__(self):
		parser=argparse.ArgumentParser(
			prog="deployShell",
			description="deployShell provides cloud-deployment automation",
			epilog="for more information, see deployshell.com"
		) 	
		parser.add_argument(
			'--logLevel',
			dest='LogLevel',
			default='INFO'
			help='set the logLevel (DEBUG,INFO,WARNING,CRITICAL)'
		)
		try:
			args=parser.parse_args()
		except Exception as err:
			raise Exception("failed to parse args.  Error:"+str(err))
		self.__setLogLevel()
		self.__user=shellUser()
		self.__activityLog=logger('activity',self.__logLevel)
		self.__errorLog=logger('errors',self.__logLevel)
		self.__shell=shellUI(self.__logLevel)
		self.__router=shellRouter(self.__logLevel)
		
	def start(self):
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
	
	
if __name__ == "__main__":
	ds=deployShell()
	ds.start()
	