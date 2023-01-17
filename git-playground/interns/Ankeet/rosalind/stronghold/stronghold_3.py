from decor import timing
#Problem 3
@timing
def func1(t):
    dict_map = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    t_needed = t.strip()
    t_needed = t_needed[::-1]
    main_l = []
    for x in range(len(t_needed)):
        main_l.append(dict_map[t_needed[x]])
    print(''.join(main_l))

@timing
def func2(t):
    t = t.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    print(t)

@timing
def func3(t):
    print(t[::-1].translate(str.maketrans('ACGT', 'TGCA')))

__all__ = [func1, func2, func3] 