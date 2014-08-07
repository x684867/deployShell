#!/usr/bin/env python
#
# shellUser.py
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
# The file tracks user information.
#
import os
import sys
import grp
import pwd
import getpass
from shellLogger import logger

class shellUser:
	__uid=0
	__username=''
	__gid=0
	__groupIds=[]
	__log=None
	
	def __init__(self):
		self.__log=logger('shellUser')
		self.__username=getpass.getuser()
		self.__uid=os.getuid()
		self.__gid=os.getgid()
		print "typeof gid: " + str(type(self.__gid))
		self.__groupIds=os.getgroups()
		
	def __del__(self):
		self.__log.write('__del__() terminating ['+str(self.__username)+"]")

	@property
	def gid(self):
		return self.__gid
		
	@property
	def userName(self):
		return self.__username

	@property
	def group(self,gid):
		return grp.getgrgid(gid).gr_name

	@property
	def groups(self):
		return self.__groupIds

	@property
	def groupName(self):
		return str(grp.getgrgid(self.__gid).gr_name)
			
	@property
	def groupNames(self):
		glist=[]
		for g in self.__groupIds:
			glist.append(grp.getgrgid(g).gr_name)
		return glist
	
	def isMember(self,gid):
		if gid in self.__groupIds:
			return True
		else:
			return False


if __name__ == "__main__":
	try:
		s=shellUser()
	except Exception as err:
		print " test#1 fail.  Error:"+str(err)
		sys.exit(1)
		
	try:
		print "username="+str(s.userName) + "\n"
	except Exception as err:
		print " test#2 fail.  Error:"+str(err)
		sys.exit(1)
		
	try:
		print "gid="+str(s.gid) + "\n"
	except Exception as err:
		print "test#3 fail.  Error:"+str(err)
		sys.exit(1)
		
	try:
		print "groupName="+str(s.groupName) + "\n"
	except Exception as err:
		print " test#4 fail.  Error:"+str(err)
		sys.exit(1)
		
	try:
		print "groupIds="+str(s.groupNames) + "\n"
	except Exception as err:
		print " test#5 fail.  Error:"+str(err)
		sys.exit(1)
				
	try:
		print "groupList="+str(s.groups) + "\n"
	except Exception as err:
		print " test#6 fail.  Error:"+str(err)
		sys.exit(1)
		
	try:
		print "isMember="+str(s.isMember(s.gid)) + "\n"
	except Exception as err:
		print " test#7 fail.  Error:"+str(err)
		sys.exit(1)

	print " all tests pass"
	sys.exit(0)
