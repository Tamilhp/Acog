
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
seq = "AAAACCCGGT"
reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))
print(reverse_complement)
