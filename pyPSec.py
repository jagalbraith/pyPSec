#!/usr/bin/env python
#Written by John Galbraith in an effort to not store plain text passwords.
#A leaked password is not a big deal with this script as long as this file is secure.
# If an attacker has this script and the password... PWND!
import pyDes
import base64
import random
import sys

# IMPORTANT!! If you change the serial_number you break ALL passwords.
# If you break all passwords, you must generate all new keys from the passwords.
# If you change a password, you must generate a new key from that password.
# This key MUST be 16 or 24 Bytes long. NO MORE! NO LESS!
# Mess with the serial_number at your own risk.
# I'm serious about this! --JG

# IF YOU ARE FIRST SETTING THIS UP, CHANGE THE SERIAL NUMBER!! DON'T LEAVE THIS!
serial_number = '123456789012345678901234'
if len(serial_number) == 24 or len(serial_number) == 16:
    pass
else:
    raise ValueError('serial_number MUST be 16 or 24 digits long!')


def encrypt_(password):
    key = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(24))
    enc_pass0 = pyDes.triple_des(key).encrypt(password, padmode=2)
    enc_pass1 = pyDes.triple_des(serial_number).encrypt(enc_pass0, padmode=2)
    return base64.b64encode(key + ',' + enc_pass1)


def decrypt_(b64hash):
    key = str(base64.b64decode(b64hash)).split(',')[0]
    enc_pass1 = str(base64.b64decode(b64hash)).split(',')[1]
    enc_pass0 = pyDes.triple_des(serial_number).decrypt(enc_pass1, padmode=2)
    return pyDes.triple_des(key).decrypt(enc_pass0, padmode=2)

passwd = sys.argv[1]
if passwd:
    print encrypt_(passwd)
