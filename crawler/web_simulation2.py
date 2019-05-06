from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


# chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')


def main_process():
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
    driver.get("http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/index.html")
    csv_file = open("./res.csv", "a+")
    writer = csv.writer(csv_file)
    writer.writerow(['title', 'time', 'content', 'url'])

    import time
    time.sleep(10)

    # js = '''document.getElementsByClassName('inputkuang1')[0].value = "工商银行";document.getElementsByTagName('button')[0].click();'''
    # driver.execute_script(js)
    driver.switch_to_window(driver.window_handles[1])
    for i in range(1500):
        print(i)
        if i >= 457:
            for j in range(12):
                try:
                    # print("1")
                    title_ref = driver.find_element_by_xpath(
                        '//*[@id="panel-page"]/div/div[2]/div[2]/div[' + str(j + 1) + ']/div/h3/a').get_attribute(
                        'href')
                    # print(title_ref)
                    url = title_ref
                    # print(url)
                    # if url.startswith('http://www.pbc.gov.cn'):
                    title, time, passage, url = get_news_piece(url)
                    writer.writerow([title, time, passage, url])
                    print(title, ',', time, ',"', passage, '",', url)
                    writer.flush()
                except BaseException:
                    pass
                continue
        js2 = '''document.querySelector('#default-result-paging > li.next > a').click();'''
        for k in range(5):
            try:
                driver.execute_script(js2)
                break
            except BaseException:
                # driver.refresh()
                driver.back()
                import time
                time.sleep(5)
                driver.refresh()
                continue
    # driver.close()


def get_news_piece(url):
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
    driver.get(url)
    title = ''
    time = ''
    passage_collection = ''
    try:
        title = driver.find_element_by_xpath(
            '//*[@class="portlet"]/div[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[1]/td/h2').text
        time = driver.find_element_by_xpath(
            '//*[@class="portlet"]/div[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td[4]').text
        passage_collection = driver.find_elements_by_xpath(
            '//*[@id="zoom"]/p')
        passage = ''
        for paragraph in passage_collection:
            passage += str(paragraph.text)

        if passage == '':
            passage_collection = driver.find_elements_by_xpath(
                '//*[@class="Section1"]/p')
            for paragraph in passage_collection:
                passage += str(paragraph.text)

        if passage == '':
            passage_collection = driver.find_elements_by_xpath(
                '//*[@id="zoom""]/div/p')
            for paragraph in passage_collection:
                passage += str(paragraph.text)
        if passage == '':
            passage_collection = driver.find_elements_by_xpath(
                '//*[@id="content""]//p')
            for paragraph in passage_collection:
                passage += str(paragraph.text)
        driver.quit()
        return title, time, passage, url
    except BaseException:
        pass


def get_real_url(url):
    url_list = url.split('//')
    url_real = url_list[0] + '//' + url_list[1] + '/' + url_list[2]
    return url_real


if __name__ == '__main__':
    main_process()
    # from scrapy import Selector
    #
    # body = '<html><head><title>Hello World</title></head><body></body></html>'
    # selector = Selector(text=body)
    # title = selector.xpath('//title/text()').extract_first()
    # print(selector.extract())
