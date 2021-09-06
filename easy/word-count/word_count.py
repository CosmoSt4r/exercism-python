def clear_word(word):
    word = word.strip().lower()

    for char in word:
        if not char.isalnum():
            word = word[1:]
        else:
            break

    for char in word[::-1]:
        if not char.isalnum():
            word = word[:-1]
        else:
            break

    return word


def count_words(sentence):
    sentence = sentence.replace(",", " ").replace("_", " ")
    sentence = [clear_word(word) for word in sentence.split() if clear_word(word)]

    counter = {}
    for word in sentence:
        if counter.get(word):
            counter[word] += 1
        else:
            counter[word] = 1

    return counter
