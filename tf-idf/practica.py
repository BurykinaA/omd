import math
from typing import List


class CountVectorizer:
    """Класс для преобразования текстовых данных в векторы счетчиков слов."""

    def __init__(self):
        """Инициализирует объект CountVectorizer. Создает два пустых списка: feature_names и word_to_index."""
        self.feature_names = []
        self.word_to_index = {}

    def fit_transform(self, corpus: List[str]) -> List[List[float]]:
        """
        Принимает на вход корпус документов. Создает список уникальных слов (в нижнем регистре),
        а затем создает словарь, где каждому слову сопоставляется его индекс.
        Затем создает векторы для каждого документа, где каждый элемент вектора представляет количество
        вхождений соответствующего слова в документе.
        """
        self.feature_names = list(
            dict.fromkeys(
                word.lower() for document in corpus for word in document.split()
            )
        )
        self.word_to_index = {
            word: index for index, word in enumerate(self.feature_names)
        }
        vectors = []
        for document in corpus:
            vector = [0] * len(self.feature_names)
            words = document.split()
            for word in words:
                vector[self.word_to_index[word.lower()]] += 1
            vectors.append(vector)

        return vectors

    def get_feature_names(self):
        """Возвращает список уникальных слов, которые были найдены при последнем вызове fit_transform."""
        return self.feature_names


class TfidfTransformer:
    """Класс для преобразования матрицы счетчиков слов в TF-IDF представление."""

    def tf_transform(self, count_matrix: List[List[float]]) -> List[List[float]]:
        """
        Принимает на вход матрицу счетчика (результат работы CountVectorizer) и преобразует ее в матрицу TF
        (частотность терминов), где каждый элемент делится на сумму всех элементов в этом документе.
        """
        vectors = []
        for vec in count_matrix:
            all_sum = sum(vec)
            vectors.append([round(element / all_sum, 3) for element in vec])

        return vectors

    def idf_transform(self, count_matrix: List[List[float]]) -> List[float]:
        """
        Принимает на вход матрицу счетчика и преобразует ее в вектор IDF (обратная частотность документа),
        где каждый элемент является логарифмом отношения общего количества документов к количеству документов,
        содержащих соответствующее слово.
        """
        vector = []
        all_doc = len(count_matrix)
        for column in zip(*count_matrix):
            vector.append(
                round(
                    math.log((all_doc + 1) / (len(column) - column.count(0) + 1)) + 1, 1
                )
            )

        return vector

    def fit_transform(self, count_matrix: List[List[float]]) -> List[List[float]]:
        """
        Принимает на вход матрицу счетчика и преобразует ее в матрицу TF-IDF,
        где каждый элемент является произведением соответствующих элементов матриц TF и IDF.
        """
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)

        for i in range(len(tf)):
            tf[i] = [round(t * id, 3) for t, id in zip(tf[i], idf)]

        return tf


class TfidfVectorizer(CountVectorizer):
    """Класс для преобразования текстовых данных в TF-IDF представление."""

    def __init__(self, transformer: TfidfTransformer):
        """
        Инициализирует объект TfidfVectorizer. Наследует все атрибуты и методы CountVectorizer и
        добавляет атрибут transformer, который является объектом TfidfTransformer.
        """
        super().__init__()
        self.transformer = transformer

    def fit_transform(self, corpus: List[str]) -> List[List[float]]:
        """
        Принимает на вход корпус документов. Сначала преобразует корпус в матрицу счетчиков слов
        с помощью метода fit_transform родительского класса CountVectorizer. Затем преобразует
        матрицу счетчиков в TF-IDF представление с помощью метода fit_transform класса TfidfTransformer.
        """
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)
    vectorizer = TfidfVectorizer(transformer)
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(tfidf_matrix)
