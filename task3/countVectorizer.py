class CountVectorizer:
    def __init__(self):
        self.feature_names = []

    def fit_transform(self, corpus):
        words_set = set()
        for document in corpus:
            words_set.update(document.split())

        self.feature_names = sorted(list(words_set))

        vectors = []
        for document in corpus:
            vector = [0] * len(self.feature_names)
            words = document.split()
            for word in words:
                if word in self.feature_names:
                    vector[self.feature_names.index(word)] += 1
            vectors.append(vector)

        return vectors

    def get_feature_names(self):
        return self.feature_names


def test_count_vectorizer():
    vectorizer = CountVectorizer()

    # Тест 1
    corpus = ["слово1 слово2 слово3", "слово2 слово3", "слово3"]
    vectors = vectorizer.fit_transform(corpus)
    assert vectors == [[1, 1, 1], [0, 1, 1], [0, 0, 1]], "Тест 1 не пройден"

    # Тест 2
    corpus = ["слово1", "слово2", "слово3"]
    vectors = vectorizer.fit_transform(corpus)
    assert vectors == [[1, 0, 0], [0, 1, 0], [0, 0, 1]], "Тест 2 не пройден"

    # Тест 3
    corpus = ["слово1 слово2", "слово2 слово3", "слово1 слово3"]
    vectors = vectorizer.fit_transform(corpus)
    assert vectors == [[1, 1, 0], [0, 1, 1], [1, 0, 1]], "Тест 3 не пройден"


def test_get_feature_names():
    vectorizer = CountVectorizer()

    # Тест 1
    corpus = ["слово1 слово2 слово3", "слово2 слово3", "слово3"]
    vectorizer.fit_transform(corpus)
    assert vectorizer.get_feature_names() == [
        "слово1",
        "слово2",
        "слово3",
    ], "Тест 1 не пройден"

    # Тест 2
    corpus = ["слово1", "слово2", "слово3"]
    vectorizer.fit_transform(corpus)
    assert vectorizer.get_feature_names() == [
        "слово1",
        "слово2",
        "слово3",
    ], "Тест 2 не пройден"

    # Тест 3
    corpus = ["слово1 слово2", "слово2 слово3", "слово1 слово3"]
    vectorizer.fit_transform(corpus)
    assert vectorizer.get_feature_names() == [
        "слово1",
        "слово2",
        "слово3",
    ], "Тест 3 не пройден"


if __name__ == "__main__":
    test_count_vectorizer()
    test_get_feature_names()
