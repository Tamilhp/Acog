#4 Rabbits and Recurrence Relations: https://rosalind.info/problems/fib/

sample_mon = 5
sample_offsprings = 3

def rabbit_count_func(mons, smallrabs):
    try:
      n1, n2 = 1, 1
      for i in range(mons - 1):
        temp = n1
        n1 = n1 + (n2 * smallrabs)
        n2 = temp
      return n2

    except Exception as error:
      return error

rabbit_count_func(sample_mon, sample_offsprings)