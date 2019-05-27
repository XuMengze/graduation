from snownlp import SnowNLP


def predict(analyze_list):
    senti = [SnowNLP(i).sentiments for i in analyze_list]
    return senti
