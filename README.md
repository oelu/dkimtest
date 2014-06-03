# DKIM Test 
Script to send dkim signed messages

## Usage

    dkimtest.py
    Send DKIM signed mails.
    
    Usage:
        dkimtest.py -r <recipient> -s <sender>         --keyfile <keyfile> --selector <selector>         --domain <domain> [--subject <subject>] [--body <body>]         [options]
    
    Options:
        -v --verbose   print verbose messages
        -p --printonly only prints the header, mail is not sent
