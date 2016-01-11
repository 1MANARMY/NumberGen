from number_gen import hash_key

D = {}

#capture a str of txt and issue a hash_key
hide_text = raw_input("Enter a message: ")
D[hash_key] = hide_text
#write to file

for k,v in D.items():
    print k, ':',v
