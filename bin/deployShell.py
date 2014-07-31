#!/usr/bin/env python
#
# deployShell.py
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
# deployShell.py -c <command> -a <argumentString>
import sys
from shellParser import shellParser
from helpViewer import helpViewer
#   
# main():
#	Parse the argument inputs and route the command
#	to the appropriate functionality.
#
def main():
	#
	help=helpClass('~/deployShell/etc/docs/')
	#
	parser=shellParser()
	#
	while true:
		#
		#Define Prompt
		parser.add_prompt("#")
		#Define the commands
		parser.add_command("show",	    desc="Display <license|copyright|version|status>.", type=str)
		parser.add_command("update",	desc="Update the deployShell.")
		parser.add_command("quit",		desc="Quit the deployShell.")
		parser.add_command("exit",		desc="Exit the deployShell.")
		parser.add_command("help",		desc="Display a help document.")
		
		parser.add_usage("license",		usage="license"
		
				 "Syntax:\n\n" + \
				 "#help <documentName>  :displays help file content.\n" + \
				 "#help list            :displays list of help documents.\n",
			type=str
		)
		parser.add_command("createServer",	help="Creates a server.
		parser.add_optional("--account", help="Identifies a cloud hosting account.",type=str)
		parser.add_argument("--recipe", help="Identifies a recipe.",type=str)
		parser.add_argument("--location", help="Identifies the location of a deployment.",type=str)
		parser.add_argument("--verbose", help="Produce verbose output.")
		
		
		#Read command line input
		#Parse command line input
		#Evaluate the parsed input and route command.
		#

		#
		#
		#
		args = parser.parse_args()
		
		if args.quit or args.exit:
			print "\nExiting...\n"
			sys.exit(1)
		elif args.license:
						
		
		if args.verbosity:
		


#	"upgrade")
#		logError "use 'update' instead."
#		;;
#	"update")
#		./bin/cmd/update
#		;;
#	*)
#		# Load /bin libraries (add-on commands and their supports).
#		if [ "$3" == "help" ]; then
#			show_help "$CMD"
#		else
#			execute_addon "$CMD" "$ARGS"
#		fi
#esac
    
if __name__ == "__main__":
	main()
else:
	raise Exception("deployShell.py must be executed directly.")
	