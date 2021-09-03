def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Code sizes don't match")
    return len([x for x, y in zip(strand_a, strand_b) if x != y])
