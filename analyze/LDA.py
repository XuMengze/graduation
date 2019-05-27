import jieba
from gensim import models
from gensim import corpora
from gensim import similarities
import xlrd
import re


def lda_res(sentences):
    jieba.load_userdict('data/dic.txt')
    print(sentences)
    # sentences = ["我喜欢吃土豆", "土豆是个百搭的东西", "我不喜欢今天雾霾的北京"]
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

    print()
    corpus_tfidf = tfidf[corpus]
    for doc in corpus_tfidf:
        print(doc)
    # vec = [(0, 1), (4, 1)]
    # index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=14)
    # sims = index[tfidf[vec]]
    # print(list(enumerate(sims)))

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

    # print(lda.log_perplexity(corpus[2:]))
    # lda2 = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=3)
    # ldaOut2 = lda2.print_topics(3)
    # print(lda2.log_perplexity(corpus[2:]))


def split_corpse():
    id_list = [3979864182687240,
               3981151339061833,
               3981671537180425,
               3984063267658011,
               3986678752142092,
               4001238078854775,
               4011362079771062,
               4011760911955354,
               4012338379834874,
               4016765355402373,
               4017563836912729,
               4017795462613874,
               4018642469895156,
               4018978684804180,
               4019257643373672,
               4019957396526056,
               4019996969365048,
               4020054750761276,
               4020414533592837,
               4024970415194969,
               4025130977393992,
               4025400302114225,
               4025830768359001,
               4026222046083748,
               4028831562172864,
               4033072459964406,
               4033090303042878,
               4035917482033207,
               4036972915705077,
               4038025179288771,
               4040022664962218,
               4051967200041858,
               4053405045333413,
               4054502396490407,
               4054877233284671,
               4055577183375498,
               4055898341443160,
               4056303879789036,
               4057039254153858,
               4057756484588849,
               4058351744308362,
               4058853098834309,
               4059978656269706,
               4060328318616657,
               4060376192092582,
               4060628374543765,
               4062826471070004,
               4063438898657222,
               4064649005639462,
               4065027281428920,
               4065029286490807,
               4065374494507024,
               4065374913181613,
               4065721833128309,
               4065977559246017,
               4067120738873068,
               4070760484220638,
               4072916460968836,
               4072978997923072,
               4073668633745080,
               4075510957031212,
               4075830482881553,
               4077340817979865,
               4078073064104219,
               4080600001991320,
               4081670409304260,
               4083119818356505,
               4083502515293266,
               4085324999061145,
               4086232214508916,
               4090740969639752,
               4091124031338953,
               4092909856635507,
               4095459506674002,
               4095818845726515,
               4095820464357772,
               4098338695887096,
               4098986715357115,
               4099442904599658,
               4100529313012471,
               4105971376108938,
               4107424182367584,
               4108525820618944,
               4109248419357967,
               4109532168278801,
               4109908292767927,
               4111630918298905,
               4115758830741550,
               4120082739595582,
               4120776959075606,
               4121544935952846,
               4121768974990147,
               4123681531216108,
               4126591560454973,
               4134246119043773,
               4135363393569561,
               4138605355910988,
               4141857447686874,
               4149447937571431,
               4149798376238336,
               4153784441660685,
               4155456831987616,
               4155557504308048,
               4155560650222247,
               4155965350172572,
               4156197491744585,
               4157282629594129,
               4157322253129073,
               4161759349115454,
               4164284336503271,
               4167205001691359,
               4168190466274301,
               4171182867672507,
               4172687141711717,
               4176819840178490,
               4180961820377895,
               4184418098819618,
               4186766502145802,
               4190034082692428,
               4195099280317904,
               4197305051244969,
               4199110107580056,
               4199172456545571,
               4200581566257447,
               4202001870983002,
               4202715716889875,
               4203060647437852,
               4206081615715131,
               4206179456356427,
               4213182341838556,
               4216536647936923,
               4217579578800399,
               4224795350926721,
               4225864855917211,
               4232295256451969,
               4240042647781696,
               4240453656804733,
               4241794621867767,
               4250160538396692,
               4252683542208882,
               4253742976592415,
               4254469942713617,
               4261457959290164,
               4261771214512245,
               4262544380478433,
               4263514312771225,
               4266003040594536,
               4268532344201847,
               4270684060868999,
               4273952061069565,
               4277737051463365,
               4280519438594280,
               4283463207131755,
               4289930962923248,
               4300904637150138,
               4315730307010980,
               4326313613765468,
               4328350338098769,
               4328660213135138,
               4330982565568991,
               4331549895592546,
               4334086112392063,
               4341461656729518,
               4346449637100411
               ]
    workbook = xlrd.open_workbook(r'data/blog.xlsx')

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始

    str_list = []
    str_list_inner = []
    pattern = re.compile(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
    pattern_mark = re.compile(r'[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）☆《》\d+年月日·：↓]+')
    for i in range(sheet1.nrows):
        if id_list.__contains__(int(sheet1.row_values(i)[2])):
            str_list.append(str_list_inner.copy())
            str_list_inner = []
        string = sheet1.row_values(i)[6].replace('#阴阳师手游[超话]#', '').replace('\n', '').replace('#阴阳师手游#', '').strip()
        string = re.sub(pattern, '', string)
        string = re.sub(pattern_mark, '', string)
        str_list_inner.append(string)
    return str_list


if __name__ == '__main__':
    sentences_list = split_corpse()
    lda_res(sentences_list[40])
