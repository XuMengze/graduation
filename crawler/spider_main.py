import requests
from lxml import etree

headers = {
    'Cookie': 'wzws_cid=033f2c1a3f06f6965ef49fd6585daf0f944654478b45282bbe7415f202df2b58f574736319e0c3275c5bba8405ad060b',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}


def get_single_news(url):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    selector = etree.HTML(r.text)
    title = selector.xpath(
        '//*[@id="10929"]/div[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/h2')[
        0].text
    time = \
        selector.xpath('//*[@id="10929"]/div[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td[4]/text()')[
            1]
    passage_collection = selector.xpath('//*[@id="zoom"]/div/p')
    passage = ''
    print(r.text)
    for p_label in passage_collection:
        passage += str(p_label.text)
    return title, time, passage


basci_str = 'http://www.pbc.gov.cn'


def get_url_list(url):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    selector = etree.HTML(r.text)
    url_list = selector.xpath('//*[@id="11040"]/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/font/a/@href')
    res_list = []
    for url in url_list:
        res_list.append(basci_str + str(url))
    return res_list


if __name__ == '__main__':
    # res = get_url_list('http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index1.html')
    res = get_single_news('http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/3786032/index.html')
    print(res)
