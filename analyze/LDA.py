import jieba
from gensim import models
from gensim import corpora
from gensim import similarities

sentences = ["我喜欢吃土豆", "土豆是个百搭的东西", "我不喜欢今天雾霾的北京"]
words = []
for doc in sentences:
    words.append(list(jieba.cut(doc)))
print(words)

dic = corpora.Dictionary(words)
print(dic)
print(dic.token2id)

corpus = [dic.doc2bow(text) for text in words]
print(corpus)

tfidf = models.TfidfModel(corpus)

vec = [(0, 1), (4, 1)]
print()
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print(doc)
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=14)
sims = index[tfidf[vec]]
print(list(enumerate(sims)))

lsi = models.LsiModel(corpus_tfidf, id2word=dic, num_topics=2)
lsiout = lsi.print_topics(2)
print(lsiout[0])
print(lsiout[1])

corpus_lsi = lsi[corpus_tfidf]
for doc in corpus_lsi:
    print(doc)

lda = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=2)
ldaOut = lda.print_topics(2)
print(ldaOut[0])
print(ldaOut[1])
corpus_lda = lda[corpus_tfidf]
for doc in corpus_lda:
    print(doc)

print(lda.log_perplexity(corpus[2:]))
lda2 = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=3)
ldaOut2 = lda2.print_topics(3)
print(lda2.log_perplexity(corpus[2:]))
