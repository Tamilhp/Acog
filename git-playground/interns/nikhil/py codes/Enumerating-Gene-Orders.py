# Enumerating Gene Orders: https://rosalind.info/problems/perm/

sample_number = 3

import itertools as it

def enumerate_gene_orders(samp_no):
  perm_list = [" ".join(i) for i in it.permutations("".join([str(i) for i in range(1, samp_no+1)]))]
  return len(perm_list), perm_list

count, perm_list = enumerate_gene_orders(5)

for i in perm_list:
  print(i)