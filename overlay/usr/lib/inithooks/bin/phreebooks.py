#!/usr/bin/python
"""Set PhreeBooks admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
import inithooks_cache
import random
import string
import hashlib

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "PhreeBooks Password",
            "Enter new password for the PhreeBooks 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "PhreeBooks Email",
            "Enter email address for the PhreeBooks 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    salt = ''.join((random.choice(string.letters+string.digits) for x in range(2)))
    hash = ':'.join([hashlib.md5(salt+password).hexdigest(), salt])

    m = MySQL()
    m.execute('UPDATE phreebooks.users SET admin_pass=\"%s\" WHERE admin_name=\"admin\";' % hash)
    m.execute('UPDATE phreebooks.users SET admin_email=\"%s\" WHERE admin_name=\"admin\";' % email)


if __name__ == "__main__":
    main()

