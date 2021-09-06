def is_pangram(sentence):
    return len([x for x in set(sentence.lower()) if 97 <= ord(x) <= 122]) == 26
