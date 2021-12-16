# Krypton0 - Walkthrough:

## Instruction:

Welcome to Krypton! The first level is easy. The following string encodes the password using Base64:

S1JZUFRPTklTR1JFQVQ=
Use this password to log in to krypton.labs.overthewire.org with username krypton1 using SSH on port 2231. You can find the files for other levels in /krypton/

## Solution:

well, let's read about base64. Apperantly it decodes/encodes using the base64 method:

nir@LAPTOP-8C4IQCNL:/mnt/c/tmp$ echo S1JZUFRPTklTR1JFQVQ= | base64 -d
KRYPTONISGREAT

Well, we're done. :)