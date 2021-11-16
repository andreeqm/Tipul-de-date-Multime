def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
l = ["A","B","C","D"]
r = [x for x in powerset(l)]
r.sort()
print (r)
