# Krypton3 - Walkthrough

## Instruction

Well done.  You've moved past an easy substitution cipher.

Hopefully you just encrypted the alphabet a plaintext
to fully expose the key in one swoop.

The main weakness of a simple substitution cipher is
repeated use of a simple key.  In the previous exercise
you were able to introduce arbitrary plaintext to expose
the key.  In this example, the cipher mechanism is not
available to you, the attacker.

However, you have been lucky.  You have intercepted more
than one message.  The password to the next level is found
in the file 'krypton4'.  You have also found 3 other files.
(found1, found2, found3)

You know the following important details:

- The message plaintexts are in English (*** very important)
- They were produced from the same key (*** even better!)


Enjoy.

## Solution

krypton3@krypton:/krypton/krypton3$ ls -la
total 36
drwxr-xr-x 2 root     root     4096 May 19  2020 .
drwxr-xr-x 8 root     root     4096 May 19  2020 ..
-rw-r----- 1 krypton3 krypton3 1542 May 19  2020 found1
-rw-r----- 1 krypton3 krypton3 2128 May 19  2020 found2
-rw-r----- 1 krypton3 krypton3  560 May 19  2020 found3
-rw-r----- 1 krypton3 krypton3   56 May 19  2020 HINT1
-rw-r----- 1 krypton3 krypton3   37 May 19  2020 HINT2
-rw-r----- 1 krypton3 krypton3   42 May 19  2020 krypton4
-rw-r----- 1 krypton3 krypton3  785 May 19  2020 README

I created a python script to print the frequencies of each letter, and sort it.

The original alphabet frequency:

E	11.1607% 56.88	M	3.0129%	15.36
A	8.4966%	43.31	H	3.0034%	15.31
R	7.5809%	38.64	G	2.4705%	12.59
I	7.5448%	38.45	B	2.0720%	10.56
O	7.1635%	36.51	F	1.8121%	9.24
T	6.9509%	35.43	Y	1.7779%	9.06
N	6.6544%	33.92	W	1.2899%	6.57
S	5.7351%	29.23	K	1.1016%	5.61
L	5.4893%	27.98	V	1.0074%	5.13
C	4.5388%	23.13	X	0.2902%	1.48
U	3.6308%	18.51	Z	0.2722%	1.39
D	3.3844%	17.25	J	0.1965%	1.00
P	3.1671%	16.14	Q	0.1962%	(1)

Our frequency in `found1`:
S - 10.05%
C - 6.94%
Q - 6.87%
J - 6.61%
U - 6.49%
B - 5.64%
G - 5.25%
N - 4.80%
D - 4.47%
Z - 3.70%
V - 3.63%
W - 3.05%
Y - 2.72%
T - 2.08%
X - 1.88%
M - 1.88%
L - 1.75%
K - 1.62%
A - 1.30%
E - 1.10%
F - 0.71%
O - 0.45%
I - 0.13%
H - 0.13%
R - 0.06%
P - 0.00%

`found2`:
S - 11.42%
Q - 8.74%
J - 7.42%
N - 6.34%
U - 6.11%
B - 6.06%
D - 5.59%
G - 5.22%
C - 4.04%
W - 3.10%
Z - 2.77%
V - 2.49%
M - 2.11%
T - 1.74%
E - 1.60%
Y - 1.55%
X - 1.55%
K - 1.41%
L - 1.27%
A - 1.22%
I - 0.66%
F - 0.56%
O - 0.14%
R - 0.09%
H - 0.09%
P - 0.05%

`found3`:
S - 10.36%
Q - 8.57%
J - 7.32%
G - 6.25%
C - 6.07%
N - 5.54%
B - 5.36%
U - 4.82%
D - 3.93%
V - 3.75%
Z - 2.86%
W - 2.86%
E - 2.32%
M - 2.14%
K - 2.14%
Y - 1.61%
X - 1.61%
A - 1.61%
T - 1.07%
L - 1.07%
F - 0.89%
I - 0.54%
O - 0.36%
R - 0.18%
P - 0.18%
H - 0.00%

Therefore we conclude:
S -> E
Q -> A
J -> R

and now what? find frequencies of double letters? most unrecent letter?

Well... Let's cut the bullshit.
We have a online solver:
https://www.dcode.fr/monoalphabetic-substitution
any means necessary!

Here's the output
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B O I H G K N Q Z T W Y U R X J A V E M S L D F P C

Therefore, out string to decrypt is:
KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS

which is:
WELL DONE THE LEZEL FOUR PASSWORD IS BRUTE

(probably using found2 and found3 would solve the 'z' error - lezel)

FINISHED!