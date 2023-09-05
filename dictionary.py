from PyMultiDictionary import MultiDictionary

dict = MultiDictionary()

# === FUNCTIONS ===

def prGr(skk): print("\033[32m{}\033[00m" .format(skk))
def prRed(skk): print("\033[31m{}\033[00m" .format(skk))

def welcome():
	prGr("Select: (1) (2) (3)")
	prGr("(1) Select language: 'en', 'fr'")
	prGr("(2) Select mode: 'def', 'syn', 'ant', 'tra'")
	prGr("(3) Select word")
	prGr("(quit 'q')")

def definition(l,w):
	print("\n(fr) Definitions of %s :\n" % w)
	print(dict.meaning(l,w))

def synonym(l,w):
	print("\n(fr) Synonyms of %s :\n" % w)
	print(dict.synonym(l,w))

def antonym(l,w):
	print("\n(fr) Antonyms of %s :\n" % w)
	print(dict.antonym(l,w))

def translation(l,w):
	print("\n(fr) Translation of %s :\n" % w)
	print(dict.translate(l,w))

def switch(k):
	keys = k.split()
	if len(keys)>3: prRed("Error: too many words")

	lan = keys[0]
	mode = keys[1]
	word = keys[2]

	if 'q' in keys:
		return
	
	if not(lan=='en' or lan=='fr'):
		prRed("(1) Error: wrong language")
		return

	if mode=='def':
		definition(lan, word)
	elif mode=='syn':
		synonym(lan, word)
	elif mode=='ant':
		antonym(lan, word)
	elif mode=='tra':
		translation(lan, word)
	else:
		prRed("\nError: wrong mode")
		return

	return


# === MAIN ===

print('\n\t--- Dictionary ---')
welcome()
key = input("Select: ")
switch(key)
print('\n')


# print(dict.meaning('en', 'good'))
# print(dict.synonym('es', 'Bueno'))
# print(dict.antonym('en', 'Life'))
# print(dict.translate('en', 'Range'))

# Supported dictionaries
# DICT_EDUCALINGO: Meaning, synonym, translation for all languages
# DICT_SYNONYMCOM: Synonyms and Antonyms (English)
# DICT_THESAURUS: Synonyms (English)
# DICT_WORDNET: Meanings (English)