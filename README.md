# DKIM Test 
Script to send DKIM signed messages

## Requirements
Requires the folowing non-standard pyton modules: 
* dkimpy
* docopt

## Usage

    dkimtest.py
    Send DKIM signed mails.
    
    Usage:
        dkimtest.py -r <recipient> -s <sender>         --keyfile <keyfile> --selector <selector>         --domain <domain> [--subject <subject>] [--body <body>]         [options]
    
    Options:
        -v --verbose   print verbose messages
        -p --printonly only prints the header, mail is not sent
