def abbreviate(words):
    words = words.replace("_", " ").replace(",", " ").replace("-", " ")
    return "".join(word[0].upper() for word in words.split())
