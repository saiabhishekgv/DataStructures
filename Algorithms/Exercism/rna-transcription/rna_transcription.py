def to_rna(dna_strand):
    d = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    s = ''
    for i in range(len(dna_strand)):
        s += d[dna_strand[i]]

    return s
