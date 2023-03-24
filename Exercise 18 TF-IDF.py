import numpy as np
import math

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def main(text):

    docs = [line.split() for line in text.splitlines()]
    N = len(docs)
    words = list(set(text.split()))

    df = {}
    tf = {}
    for word in words:
        tf[word] = [doc.count(word) / len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs]) / N

    tfidf = []
    for doc_index, doc in enumerate(docs):
        tfidf.append([])
        for word in words:
            tfidf[doc_index].append(tf[word][doc_index] * math.log(1 / df[word], 10))

    dist = np.empty((N, N), dtype=float)
    for i in range(N):
        for j in range(N):
            if (i == j):
                dist[i][j] = np.inf
            else:
                dist[i][j] = 0
                for x in range(len(tfidf[i])):
                    dist[i][j] += abs(tfidf[i][x] - tfidf[j][x])
    print(np.unravel_index(np.argmin(dist), dist.shape))

main(text)
