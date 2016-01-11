#!/usr/bin/python
from number_gen import hash_key
import sys, getopt

#version = 1.0.0
#output_filename = 'main.py'

D = {}
def main(argv):
    try:
	options, remainder  = getopt.getopt(argv, "mp:", ['message=','pull'])
    except getopt.GetoptError:
        print 'Error: Type main.py -h for help.'
	sys.exit(2)
    for opt, arg in options:
	if opt in ('-m', '--message'):
            #capture a str of txt and issue a hash_key
            hide_text = raw_input("Enter a message: ")
            D[hash_key] = hide_text
            print D
            #write to file

	elif opt in ('-p', '--pull'):
	    #print to screen and pull with key
            for k,v in D.items():
                if k == hide_text:
	            print "Your Message: " + v
	else:
            print 'main.py -m <"message"> -p <key>'
            sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
