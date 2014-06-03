#!/usr/local/bin/python2.7
""" dkimtest.py
Send DKIM signed mails.

Usage:
    dkimtest.py -r <recipient> -s <sender> \
        --keyfile <keyfile> --selector <selector> \
        --domain <domain> [--subject <subject>] [--body <body>] \
        [options]

Options:
    -v --verbose   print verbose messages
    -p --printonly only prints the header, mail is not sent

"""
__author__ = 'olivier'

import smtplib
from smtplib import SMTPException
import sys
from email.message import Message
from pprint import pprint

from dkim import sign
from docopt import docopt


def send_mail(recipient,
              sender,
              selector,
              keyfile,
              domain,
              body="DKIM Test Message",
              subject="DKIM Test Message",
              printonly=False):
    """
    Sends a DKIM signed E-Mail.

    recipient   recipient address
    sender      sender address
    selector    DKIM selector
    keyfile     file containing the private key
    domain      sending domain
    body        e-mail message body
    subject     e-mail subject
    printonly   print only the header, do not send mail
    """
    try:
        private_key = open(keyfile).read()
    except IOError, ex:
        print "Error: file %s is not readable " % (keyfile)
        print ex.message
        sys.exit(2)

    # compose message
    msg = Message()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_payload(body)

    # sign message
    email = msg.as_string()
    sig = sign(email,
               selector,
               domain,
               private_key)
    dkimmail = sig + email
    printverbose("Message is: ")
    printverbose(dkimmail)

    if printonly:
        print dkimmail
    else:
        try:
            server = smtplib.SMTP('localhost')
            if VERBOSE:
                server.set_debuglevel(1)
            server.sendmail(sender, recipient, dkimmail)
            print "Successfully sent email"
        except SMTPException:
            print "Error: unable to send email"


def printverbose(msg):
    """
    prints a message if global variable Verbose=True
    """
    if VERBOSE:
        pprint(msg)


def main():
    """
    main function
    """
    global VERBOSE
    # gets arguments from docopt
    arguments = docopt(__doc__)
    # assigns docopt arguments
    sender = arguments['<sender>']
    recipient = arguments['<recipient>']
    keyfile = arguments['<keyfile>']
    selector = arguments['<selector>']
    domain = arguments['<domain>']
    VERBOSE = arguments['--verbose']
    printonly = arguments['--printonly']

    printverbose(arguments)
    send_mail(recipient, sender, selector, keyfile, domain, printonly)


if __name__ == "__main__":
    main()
