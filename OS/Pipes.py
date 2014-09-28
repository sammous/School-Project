__author__ = 'MACSAMI'

import os
import sys

from random import randrange

#print "The child will write text to a pipe and "
#print "the parent will read the text written by child..."

# file descriptors r, w for reading and writing
r, w = os.pipe()


processId = os.fork()
pid = processId
numeroFils = 0
nombreSigne = 10


if pid != 0:
    # This is the parent process
    # Closes file descriptor w
    os.close(w)
    r = os.fdopen(r)
    print "Parent's pid is", os.getpid()
    str = r.read()
    print str
    sys.exit(0)
else:
    # This is the child process
    os.close(r)
    #Create second child
    numeroFils = 1
    processId2 = os.fork()
    pid = processId2
    if pid == 0:
        numeroFils = 2
    w = os.fdopen(w, 'w')
    #Constructing list
    listSigne = []
    for i in range(nombreSigne):
        a = randrange(2)
        if a == 1:
            listSigne.append("+")
        else:
            listSigne.append("-")
    print "Child number %s pid is" % numeroFils + " %s" %os.getpid() + "\n"

    print listSigne
    if numeroFils == 1:  #Actions done by child 1
        for l in listSigne:
            if l == "-":
                print "- removed"
                listSigne.remove(l)
        w.write("Number of + is %s \n" %len(listSigne))
    else:                #Actions done by child 2
        for l in listSigne:
            if l == "+":
		print "+ removed"
                listSigne.remove(l)
        w.write("Number of - is %s \n" %len(listSigne))
    w.close()
    print "Child closing"
    sys.exit(0)

