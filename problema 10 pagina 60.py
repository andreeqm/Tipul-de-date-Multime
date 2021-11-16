def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
l = [1, 2, 3, 4]
r = [x for x in powerset(l)]
r.sort()
print (r)
