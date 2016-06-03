# pyPSec
Python Password Storing System

To Do:

1. Write a new serial number function that stores SN in an encrypted file.

Setup:

1. Download pyPSec.py
2. Open it and change the serial number. It has to be a 16 or 24 digits in length. If you don't change your SN, anyone can crack your password hashes if they get them. CHANGE YOUR SERIAL NUMBER!! Make it hard too.



Usage:

1. To encrypt a password call pyPSec.py from command line and feed it a password.
python pyPSec.py myPassword123
Copy the hash and store that in your script.


2. To use the encrypted hash in your script:

import pyPSec
hash = 'N0ZETDVpRU0yYThrdmpsSnBnRlN2TlRYLLX+/CVXZwDBkzXML8eFwms='
pyPSec.decrypt_('hash')
