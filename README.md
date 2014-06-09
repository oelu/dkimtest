# DKIM Test 
Script to send DKIM signed messages

## Requirements
Requires the following non-standard python modules: 
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

## Usage Example
Usage example with --printonly and --verbose option set. 

    INFO: Verbose output activated.
    DEBUG: sign headers: [('from', 'me@ideaio.ch\r\n'), ('to', 'test@gmail.com\r\n'), ('subject', 'DKIM Test Message\r\n')]
    INFO: e-mail message is:
    INFO: DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=ideaio.ch; i=@ideaio.ch;
     q=dns/txt; s=ideaio; t=1402313794; h=From : To : Subject : From :
     Subject; bh=hT5oaVxW9q2TEJlR0GGG/8eM3VpznClJZQSO8lmKa0M=;
     b=K+856l4DoNm7VCpVYWmpnrlFpR6YKIr+qUAScpLljIF5vlI/7E1t/X1eKsIqGS0xWKDP0l
     zfWOnuKUzdC1cHiEZUDVznyjtph7lZF1d+nncS1QR+eqMvV+DHjgwcwdOgFicttdvHRvF8Ja
     hKs26ZfnC4bqtqrx8thjFLDbd2fRs=
    From: me@ideaio.ch
    To: test@gmail.com
    Subject: DKIM Test Message
    
    DKIM Test Message
    DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=ideaio.ch; i=@ideaio.ch;
     q=dns/txt; s=ideaio; t=1402313794; h=From : To : Subject : From :
     Subject; bh=hT5oaVxW9q2TEJlR0GGG/8eM3VpznClJZQSO8lmKa0M=;
     b=K+856l4DoNm7VCpVYWmpnrlFpR6YKIr+qUAScpLljIF5vlI/7E1t/X1eKsIqGS0xWKDP0l
     zfWOnuKUzdC1cHiEZUDVznyjtph7lZF1d+nncS1QR+eqMvV+DHjgwcwdOgFicttdvHRvF8Ja
     hKs26ZfnC4bqtqrx8thjFLDbd2fRs=
    From: me@ideaio.ch
    To: test@gmail.com
    Subject: DKIM Test Message
    
    DKIM Test Message
