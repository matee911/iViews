class Vectorizer:

    def __init__(self, fun):
        self._fun = fun

    def fit(self, mapping):
        self._sum = sum(mapping.values())

    def transform(self, rows):
        v = []
        for row in rows:
            v.append(self._vectorize_row(row))
        return v

    def _vectorize_row(self, row):
        return self._fun(self._sum, row)
