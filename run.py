#!/usr/bin/env python3
import ipdb
from random import shuffle, sample

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
	6: ['כ', 'ל', 'מ', 'ז', 'ח', 'ט', 'ב', 'ג', 'ד', 'ה', 'ק', 'ש'],
	7: ['ק', 'ר', 'ש', 'ג', 'ד', 'ה', 'ס', 'ע', 'פ', 'ז', 'ח', 'ט', 'ב'],
	8: ['ש', 'ת', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס',],
	9: ['א', 'ב', 'ט', 'י', 'כ', 'ל', 'מ', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת'],
	10: ['א', 'ב', 'צ', 'ק', 'ר', 'ש'],
	11: ['ז', 'ח', 'ט', 'י', 'ל', 'מ', 'נ'],
	12: ['צ', 'ק', 'ר', 'ש'],
	13: ['ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'ק', 'ר', 'ש'],
	14: [],
	15: ['פ', 'צ', 'ק', 'ר', 'ש', 'ת'],
	16: ['א', 'ב', 'ג', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'ע', 'פ', 'צ', ],
	17: ['ב', 'ג', 'ד', 'י', 'כ', 'ל', 'מ', 'נ', 'ס'],
	18: ['כ', 'ל', 'מ', 'ס', 'ע', 'פ'],
	19: [],
	20: [],
	21: [],
	22: [],
}

filled_guesses = dict()
for letter, guess in guesses.items():
	shuffle(all_letters)
	if guess == []:
		filled_guesses[letter] = all_letters
	else:
		filled_guesses[letter] = guess

def generate_assumption():
	unguessed = set(all_letters)
	assum = dict()
	for letter, guess in filled_guesses.items():
		possible_letters = unguessed.intersection(guess)
		if not possible_letters:
			return None
		guessed_letter = sample(possible_letters, 1)[0]
		unguessed.remove(guessed_letter)
		assum[letter] = guessed_letter
	return assum


def get_assumption(assum):
	"""assumption is an ordered list of the alphabeta so that 01 is the first item, 02 is the seconds etc."""
	if not assum:
		return
	ret = ''
	for word in text:
		for letter in word:
			ret += assum[letter]
		ret += " "
	return ret[::-1]

for i in range(1000):
	guess = get_assumption(generate_assumption())
	if guess:
		print(guess)

# ipdb.set_trace()