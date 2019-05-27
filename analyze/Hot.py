import xlrd
import re


def split_corpse_update():
    workbook = xlrd.open_workbook(r'data/blog.xlsx')
    sheet1 = workbook.sheet_by_index(0)
    str_list = []
    pattern = re.compile(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
    pattern_mark = re.compile(r'[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）☆《》\d+年月日·：↓]+')
    for i in range(sheet1.nrows):
        if str(sheet1.row_values(i)[6]).__contains__('维护更新公告'):
            blog_dict = {}
            string = sheet1.row_values(i)[6].replace('#阴阳师手游[超话]#', '').replace('\n', '').replace('#阴阳师手游#', '').strip()
            string = re.sub(pattern, '', string)
            string = re.sub(pattern_mark, '', string)
            blog_dict['blog'] = string
            blog_dict['support'] = sheet1.row_values(i)[3]
            blog_dict['repost'] = sheet1.row_values(i)[5]
            blog_dict['time'] = sheet1.row_values(i)[1]
            blog_dict['id'] = sheet1.row_values(i)[2]
            blog_dict['comment_num'] = sheet1.row_values(i)[0]
            str_list.append(blog_dict)
    return str_list


if __name__ == '__main__':
    print(split_corpse_update())
