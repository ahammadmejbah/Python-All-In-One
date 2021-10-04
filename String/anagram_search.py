import collections

# remove whitespaces
def remove_whitespace(string):
    return ''.join(string.split())

def is_anagram(string1, string2):
    charCount1 = collections.Counter(remove_whitespace(string1.lower()))
    charCount2 = collections.Counter(remove_whitespace(string2.lower()))

    allChars = set(charCount1.keys())
    allChars = allChars.union(charCount2.keys())

    for c in allChars:
        if (charCount1[c] != charCount2[c]):
            return False

    return True

# Dry runs

assert is_anagram("anagram", "not a gram") == False
assert is_anagram("anagram", "na a marg") == True
assert is_anagram("William Shakespeare", "I am \t a weakish speller") == True
assert is_anagram("Madam Curie", "Radium came") == True
assert is_anagramg("notagram", "notaflam") == False