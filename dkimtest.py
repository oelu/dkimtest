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

import logging as log
import smtplib
import sys

from email.message import Message
from smtplib import SMTPException

from dkim import sign
from docopt import docopt


# TODO: function parameters are to long, make options dict
def send_mail(recipient,
              sender,
              selector,
              keyfile,
              domain,
              body="DKIM Test Message",
              subject="DKIM Test Message",
              printonly=False,
              verbose=False):
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
    verbose     print smtp debug output
    """
    try:
        private_key = open(keyfile).read()
    except IOError, ex:
        log.error("file %s is not readable", keyfile)
        log.error(ex.message)
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
    log.info("e-mail message is:")
    log.info(dkimmail)

    if printonly:
        print dkimmail
    else:
        try:
            server = smtplib.SMTP('localhost')
            # TODO: check loglevel
            if verbose:
                log.info("smtp debug level was set to 1")
                server.set_debuglevel(1)
            server.sendmail(sender, recipient, dkimmail)
            print "Successfully sent email"
        except SMTPException:
            log.error("unable to send email")


def main():
    """
    main function
    """
    # gets arguments from docopt
    arguments = docopt(__doc__)
    # assigns docopt arguments
    sender = arguments['<sender>']
    recipient = arguments['<recipient>']
    keyfile = arguments['<keyfile>']
    selector = arguments['<selector>']
    domain = arguments['<domain>']
    verbose = arguments['--verbose']
    printonly = arguments['--printonly']

    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output activated.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    send_mail(recipient,
              sender,
              selector,
              keyfile,
              domain,
              printonly=printonly,
              verbose=verbose)


if __name__ == "__main__":
    main()
