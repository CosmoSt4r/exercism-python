def is_isogram(string):
    letters = []
    for char in string.lower():
        if char.isalpha() and char in letters:
            return False
        letters.append(char)
    return True
