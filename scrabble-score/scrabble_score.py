def score(word):
    scores = {'aeioulnrst' : 1,
              'dg' : 2,
              'bcmp' : 3,
              'fhvwy' : 4,
              'k' : 5,
              'jx' : 8,
              'qz' : 10,}

    count = 0
    for char in word.lower():
        for letters in scores.keys():
            if char in letters:
                count += scores.get(letters)

    return count
