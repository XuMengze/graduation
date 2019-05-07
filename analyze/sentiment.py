import pandas as ps
from snownlp import SnowNLP
import csv
from snownlp import sentiment


def construct_dict():
    fs = ps.read_excel('sample.xls')
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
    senti = [SnowNLP(i).sentiments for i in analyze_list if len(i) > 2]
    noun = [i[0] for i in SnowNLP(analyze_str[:-2]).tags if i[1] == 'n']

    res = 'no_trend'
    if len(senti) > 2:
        if senti[0] > 0.65:
            res = 'pos'
        elif len(senti) > 4 and (senti[0] + senti[1] + senti[2]) / 3 - (senti[-1] + senti[-2] + senti[-3]) / 3 > 0.3:
            res = 'pos'
        elif (senti[0] + senti[1]) / 2 < 0.4:
            res = 'neg'

    return senti, res, noun


if __name__ == '__main__':
    dict = construct_dict()
    csv_file = open("./res.csv", "w")
    writer = csv.writer(csv_file)
    i = 0
    for k in dict.keys():
        senti, trend = predict(dict[k])
        writer.writerow([k, dict[k], senti, trend])
