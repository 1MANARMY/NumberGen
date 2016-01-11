#!/usr/bin/python
from number_gen import hash_key
import sys, getopt, json

#version = 1.0.0
#output_filename = 'main.py'

D = {}
def main(argv):
    try:
	options, remainder  = getopt.getopt(argv, "mp", ['message','pull'])
    except getopt.GetoptError:
        print 'Error: Type main.py -h for help.'
	sys.exit(2)
    for opt, arg in options:
	if opt in ('-m', '--message'):
            #capture a str of txt and issue a hash_key
            hide_text = raw_input("Enter a message: ")
            D[hash_key] = hide_text
            print D.split('.')
            #write to file
	    json.dump(D, open("file.txt", 'w'))

	elif opt in ('-p', '--pull'):
	    search_key = raw_input("Enter a key: ")
	    #print to screen and pull with key
		
            for obj in json.loads(open("file.txt")):
		print obj
                h_key = obj['hash_key'].split('.')[0]
		m_val = obj['hide_text']
		if search_key == h_key:
	            print "Your Message: " + m_val
	else:
            print 'main.py -m <"message"> -p <key>'
            sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
