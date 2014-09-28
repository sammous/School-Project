__author__ = 'MACSAMI'

import os

nombreProcessus = 10

newpid = os.fork()
pid = newpid

for i in range(nombreProcessus):
    if pid != 0:
        newpid2 = os.fork()
        pid = newpid2




