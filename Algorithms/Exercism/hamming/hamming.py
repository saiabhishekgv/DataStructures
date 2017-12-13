def distance(strand_a, strand_b):
    l = len(strand_a)
    m = len(strand_b)
    if l!=m:
        raise ValueError("Two Lengths should be same")

    t_distance = 0

    for i in range(l):
        if strand_a[i]!=strand_b[i]:
            t_distance += 1

    return t_distance
