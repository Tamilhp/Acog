from decor import timing
#Problem 5
@timing
def func1(s):
    prev_str = ""
    k = s.strip().split('>')
    k.pop(0)
    max = -1000
    trial_needed = ""
    for elem in k:
        spl = elem.split('\n')
        cnt = ""
        for x in range(1, len(spl)):
            cnt += spl[x]
        perc = (cnt.count('G') + cnt.count('C'))/len(cnt)
        if max < perc:
            max = perc
            trial_needed = spl[0]
    
    print(trial_needed)
    print(max * 100)


@timing
def func2(s):
    d = {}
    for seqblock in s.split(">")[1:]:
        parts = seqblock.split("\n")
        fasta = parts[0]
        seq = ''.join(parts[1:])
        gc = 100 * ( seq.count("G") + seq.count("C") ) / float(len(seq))
        d[gc] = fasta
    print(d[max(d)])
    print(max(d))

__all__ = [func1, func2]