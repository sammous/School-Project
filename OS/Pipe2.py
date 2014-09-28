__author__ = 'MACSAMI'

import os
import sys
import time

from random import randrange

#print "The child will write text to a pipe and "
#print "the parent will read the text written by child..."

# file descriptors r, w for reading and writing
r, w = os.pipe()
r2, w2 = os.pipe()

processId = os.fork()
pid = processId
childNumber = 0
numberOfSignToSend = 20
counterPlus = 0
counterMinus = 0


if pid != 0:
    # This is the parent process
    # Closes file descriptor r
    os.close(r)
    os.close(r2)

    w = os.fdopen(w, 'w')
    w2 = os.fdopen(w2, 'w2')

    print "Parent's pid is %s \n" % os.getpid()

    #Send sign to pipes
    for i in range(numberOfSignToSend):
        if randrange(2) == 1:
            print "Parent sent + in both pipes \n"
            w.write("+")
            w2.write("+")
        else:
            print "Parent sent - in both pipes \n"
            w.write("-")
            w2.write("-")
    w.close()
    w2.close()
    sys.exit(0)
else:
    # This is the child process
    os.close(w)
    os.close(w2)
    r = os.fdopen(r)
    r2 = os.fdopen(r2)
    #Create second child
    childNumber = 1
    processId2 = os.fork()
    pid = processId2
    if pid == 0:
        childNumber = 2
    print "Child number %s pid is %s\n" % (childNumber, os.getpid())
    if childNumber == 2:
        str2 = r2.read()
        print "Flow in second pipe"
        for l in str2:
            if l == "-":
		counterMinus += 1
                print l
	print "Nomber of minus received :%s" % counterMinus
    else:
        str = r.read()
        print "Flow in first pipe"
        for l in str:
            if l == "+":
		counterPlus += 1
                print l
	print "Nomber of plus received :%s" % counterPlus
    print "Child number %s closing" % childNumber
    sys.exit(0)
