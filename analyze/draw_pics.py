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
    explode = [0.1, 0.1, 0.1]  # 0.1 凸出这部分，
    color_dict = {'pos': 'green', 'neg': 'red', 'no_trend': 'yellow'}
    colors = []
    for tr in labels:
        colors.append(color_dict[tr.split('(')[0]])
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6, colors=colors)
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


def word_counr(word_list):
    word_count_dict = {}
    print()


if __name__ == '__main__':
    file = pd.read_csv('res_by.csv')
    dict_count = {'pos': 0, 'neg': 0, 'no_trend': 0}
    dict_content_noun = {'pos': [], 'neg': [], 'no_trend': []}

    for i in range(len(file)):
        dict_count[file['trend'][i]] = dict_count[file['trend'][i]] + 1
        dict_content_noun[file['trend'][i]].extend(
            file['noun'][i][1:-1].replace('\'', '').split(','))

    # export_cloud_pic(','.join(dict_content_noun['pos']), 'pic/pos.png')
    # export_cloud_pic(','.join(dict_content_noun['neg']), 'pic/neg.png')

    label_list = []
    num_list = []
    for k in dict_count.keys():
        label_list.append(k + '(' + str(dict_count[k]) + ')')
        num_list.append(dict_count[k])
    export_pie(label_list, num_list, title='Three Trends Count')
