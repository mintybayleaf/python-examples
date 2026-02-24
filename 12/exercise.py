import operator


class Counter:
    def __init__(self, sequence):
        self.insides = {}

        for item in sequence:
            self.insides.setdefault(item, 0)
            self.insides[item] += 1

    def biggest(self):
        max_key, max_val = hash(None), -1
        for k, v in self.insides.items():
            if v > max_val:
                max_key, max_val = k, v
        return (max_key, max_val)


def max_letter(words):
    counts = [Counter(word).biggest() for word in words]
    sitems = sorted(counts, key=operator.itemgetter(1), reverse=True)
    if len(sitems):
        return sitems[0][0]


SAMPLES = [[], ["abcc"], ["aaaaa", "bbbb", "ccc"], ["bailey", "tacocat", "word"]]

print([max_letter(sample) for sample in SAMPLES])
