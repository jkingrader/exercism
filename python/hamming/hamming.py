def distance(strand_a, strand_b):

    strand_distance = 0

    if len(strand_a) != len(strand_b):
        raise ValueError(f"Length of strand_a ({len(strand_a)}) must equal length of strand_b ({len(strand_b)})")
    else:
        if len(strand_a) > 0:
            # for x in list(zip(strand_a, strand_b)):
            #     if (x[0] != x[1]):
            #         strand_distance += 1       
            strand_distance = sum([1 if x[0] != x[1] else 0 for x in list(zip(strand_a, strand_b))])
        return strand_distance
