#!/usr/bin/env python3
from random import shuffle

all_letters = list('אבגדהוזחטיכלמנסעפצקרשת')
crypt = list(range(1,23))
orig = '11-12-05-06 11-10-09-08-07-06-05-04-03'
crypt_words = orig.split(" ")
text = [[int(letter) for letter in word.split("-")] for word in crypt_words]

guesses = {
	1: ['ח', 'ט', 'י', 'כ', 'ל', 'מ', 'ס', 'ע', 'פ', 'צ'],
	2: ['ז', 'ח', 'ט', 'ב', 'ג', 'ד', 'ק', 'ר', 'ש'],
	3: ['א', 'ב', 'ג'],
	4: ['ש', 'ת', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט'],
	5: ['כ', 'ל', 'מ', 'י', 'נ', 'ס'],
	6: ['כ', 'ל', 'מ', 'ז', 'ח', 'ט', 'ב', 'ג', 'ד', 'ה', 'ק', 'ק', 'ש'],
	7: ['ק', 'ר', 'ש', 'ג', 'ד', 'ה', 'ס', 'ע', 'פ', 'ז', 'ח', 'ט', 'ב'],
	8: [],
	9: [],
	10: [],
	11: [],
	12: [],
	13: [],
	14: [],
	15: [],
	16: [],
	17: [],
	18: [],
	19: [],
	20: [],
	21: [],
	22: [],
}


def get_assumption(assum):
	"""assumption is an ordered list of the alphabeta so that 01 is the first item, 02 is the seconds etc."""
	ret = ''
	for word in text:
		for letter in word:
			ret += assum[letter]
		ret += " "
	return ret[::-1]

print(get_assumption(all_letters))