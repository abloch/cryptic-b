#!/usr/bin/env python3
from random import shuffle

all_letters = list('אבגדהוזחטיכלמנסעפצקרשת')
crypt = list(range(1,23))
orig = '11-12-05-06 11-10-09-08-07-06-05-04-03'
crypt_words = orig.split(" ")
text = [[int(letter) for letter in word.split("-")] for word in crypt_words]

shuffle(all_letters)

def get_assumption(assum):
	"""assumption is an ordered list of the alphabeta so that 01 is the first item, 02 is the seconds etc."""
	ret = ''
	for word in text:
		for letter in word:
			ret += assum[letter]
		ret += " "
	return ret[::-1]

print(get_assumption(all_letters))