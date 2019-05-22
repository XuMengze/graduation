from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *


def export_cloud_pic(text, path):
    wc = WordCloud(
        background_color="white",
        max_words=200,
        font_path="font/MSYH.ttf",
        min_font_size=15,
        max_font_size=50,
        width=800,
        height=400
    )
    wc.generate(text)
    wc.to_file(path)


def export_pie(label, num, title):
    labels = label
    fracs = num
    explode = [0, 0, 0]  # 0.1 凸出这部分，
    color_dict = {'pos': 'green', 'neg': 'red', 'no_trend': 'orange'}
    colors = []
    for tr in labels:
        colors.append(color_dict[tr.split('(')[0]])
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
    '''
    labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    shadow，饼是否有阴影
    startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    pctdistance，百分比的text离圆心的距离
    patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
    '''
    plt.title(title)
    plt.show()


def word_count(words):
    res = ''
    word_count_dict = {}
    for word in words:
        if not word_count_dict.keys().__contains__(word.strip(' ')):
            word_count_dict[word.strip(' ')] = 1
        else:
            word_count_dict[word.strip(' ')] = word_count_dict[word.strip(' ')] + 1
    res_dict = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)
    count = 0
    for i in range(100):
        if len(res_dict[i][0]) >= 2:
            res = res + res_dict[i][0] + ':' + str(res_dict[i][1]) + ','
            count = count + 1
        if count >= 10:
            break
    return res[0:-1]


if __name__ == '__main__':
    file = pd.read_csv('res_by.csv')
    dict_count = {'pos': 0, 'neg': 0, 'no_trend': 0}
    dict_notrend_count = {'single': 0, 'not_single': 0}
    dict_content_noun = {'pos': [], 'neg': [], 'no_trend': []}

    for i in range(len(file)):
        dict_count[file['trend'][i]] = dict_count[file['trend'][i]] + 1
        dict_content_noun[file['trend'][i]].extend(
            file['noun'][i][1:-1].replace('\'', '').split(','))
        if file['trend'][i] == 'no_trend':
            if len(file['content'][i][0:-2].split('||')) > 1:
                dict_notrend_count['not_single'] = dict_notrend_count['not_single'] + 1
            else:
                dict_notrend_count['single'] = dict_notrend_count['single'] + 1
    for i in range(len(dict_content_noun['pos'])):
        dict_content_noun['pos'][i] = dict_content_noun['pos'][i].strip(' ')
    for i in range(len(dict_content_noun['neg'])):
        dict_content_noun['neg'][i] = dict_content_noun['neg'][i].strip(' ')

    # export_cloud_pic(','.join(dict_content_noun['pos']), 'pic/pos2.png')
    # export_cloud_pic(','.join(dict_content_noun['neg']), 'pic/neg2.png')

    label_list = []
    num_list = []
    for k in dict_count.keys():
        label_list.append(k + '(' + str(dict_count[k]) + ')')
        num_list.append(dict_count[k])

    # label_list2 = []
    # num_list2 = []
    # for k in dict_notrend_count.keys():
    #     label_list2.append(k + '(' + str(dict_notrend_count[k]) + ')')
    #     num_list2.append(dict_notrend_count[k])

    export_pie(label_list, num_list, 'Three')
    # res_pos = word_count(dict_content_noun['pos'])
    # res_neg = word_count(dict_content_noun['neg'])
    # print(res_neg)
    # print(res_pos)
