import pandas as pd
from snownlp import SnowNLP
import csv
from snownlp import sentiment


def construct_dict():
    fs = pd.read_excel('full_topic_service.xlsx')
    res = fs.groupby('id')
    group_by_dict = {}
    for row in res:
        single_str = ''
        for single_item in row[1]['content'].index:
            single_str = single_str + str(row[1]['content'][single_item]) + '||'
        group_by_dict[row[0]] = single_str
    return group_by_dict


def train_material():
    sentiment.train('neg.txt', 'pos.txt')
    sentiment.save('sentiment.marshal')


def predict(analyze_str):
    # analyze_str = '查询卡号||中间几位记不住了||621226中间记不住，尾号9899||人呢||公积金贷款我忘记存钱进去，今天扣款没有扣全，可否再帮忙扣一次，要还款||好的，谢谢了||12||'
    # analyze_str = '你好，请问北京六道口附近有没有网点可以兑换泰铢？||还可以自助办的吗？||[4]查询网点/自助机具方法||4||中关村东升路支行||没有问题||'

    analyze_list = analyze_str[:-2].split('||')
    analyze_list.reverse()
    senti = [SnowNLP(i).sentiments for i in analyze_list]
    noun = [i[0] for i in SnowNLP(analyze_str[:-2]).tags if i[1] == 'n']

    sen_value = SnowNLP(analyze_str).sentiments
    avg_senti = 0
    if len(senti) > 0:
        for i in senti:
            avg_senti = avg_senti + i
        avg_senti = avg_senti / len(senti)
    else:
        print(analyze_str)

    # 默认为no_tread，如果对话只有一句话，则不需要处理
    res = 'no_trend'
    # 如果对话有2或3句话，则用最后一句话的情绪值减去第一句话的情绪值，判断差值所属范围；
    # 如果大于三句话，则用后三句话平均减去前三句话平均，判断差值所属范围
    if len(senti) == 2 or len(senti) == 3:
        res = 'pos' if senti[0] - senti[-1] > 0.2 else ('neg' if senti[0] - senti[-1] < -0.2 else 'no_trend')
    elif len(senti) > 3:
        if (senti[0] + senti[1] + senti[2]) / 3 - (senti[-1] + senti[-2] + senti[-3]) / 3 > 0.2:
            res = 'pos'
        elif (senti[0] + senti[1] + senti[2]) / 3 - (senti[-1] + senti[-2] + senti[-3]) / 3 < -0.2:
            res = 'neg'
    return senti, res, noun, sen_value, avg_senti


if __name__ == '__main__':
    dict = construct_dict()
    df = pd.DataFrame(columns=["id", "content", "sentiment", "trend", "sen_value", "avg_senti", "noun"])
    i = 0
    for k in dict.keys():
        senti, trend, noun, sen_value, avg_senti = predict(dict[k])
        df.loc[i] = [str(k), dict[k], senti, trend, sen_value, avg_senti, noun]
        i = i + 1
    df.to_excel("res.xls")
