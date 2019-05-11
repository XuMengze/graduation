from wordcloud import WordCloud
import pandas as pd


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


if __name__ == '__main__':
    file = pd.read_csv('res_by.csv')
    dict_count = {'pos': 0, 'neg': 0, 'no_trend': 0}
    dict_content_noun = {'pos': [], 'neg': [], 'no_trend': []}

    for i in range(len(file)):
        # dict_count[file['trend'][i]] = dic？t_count[file['trend'][i]] + 1
        dict_content_noun[file['trend'][i]].extend(
            file['noun'][i][1:-1].replace('\'', '').split(','))

    export_cloud_pic(','.join(dict_content_noun['pos']), 'pic/pos.png')
    export_cloud_pic(','.join(dict_content_noun['neg']), 'pic/neg.png')
