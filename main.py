#!/usr/bin/python
from number_gen import hash_key
import sys, getopt

D = {}
def main(argv):
    try:
	opts, args = getopt.getopt(argv, "m:p")
    except getopt.GetoptError:
        print 'Error: Type main.py -h for help.'
	sys.exit(2)
    for opt, arg in opts:
	if opt == '-m':
            #capture a str of txt and issue a hash_key
            hide_text = raw_input("Enter a message: ")
            D[hash_key] = hide_text
            #write to file

	elif opt == 'p':
	    #print to screen and pull with key
            for k,v in D.items():
                if k == hide_text:
	            print "Your Message: " + v
	else:
            print 'main.py -m <"message"> -p <key>'
            sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
