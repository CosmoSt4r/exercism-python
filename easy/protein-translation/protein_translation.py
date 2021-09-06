"""
Solution to Protein Translation task on Exercism

https://exercism.org/tracks/python/exercises/protein-translation
"""


def proteins(strand):
    """
    Get translation from RNA sequence to proteins
    """

    codons = {
        "AUG": "Methionine",
        "UUU UUC": "Phenylalanine",
        "UUA UUG": "Leucine",
        "UCU UCC UCA UCG": "Serine",
        "UAU UAC": "Tyrosine",
        "UGU UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA UAG UGA": "STOP",
    }

    result = []
    for i in range(0, len(strand), 3):
        for key, value in codons.items():
            if strand[i : i + 3] in key:
                if value == "STOP":
                    return result
                result.append(value)
    return result
