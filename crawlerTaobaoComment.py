# _*_ coding:utf-8 _*_
# @FileName : crawlerTaobaoComment.PY
# @time     : 2020/9/7 11:14
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090901
# @UpDate   : 202009010
# @Description:
# 主要功能：爬取淘宝评论，下载原始数据

import requests
from dataProcess import DataProcess
from settings import Settings

import time
import json
import re
import filePreRegular
import os

settings = Settings()
dataProcess = DataProcess()

class CrawlerTaobaoComment:

    # def __init__(self):
    #     self.filePath = settings.shopItemsOnePageCommPath

    def get_items_comm(self,inputFilePath, items_id, currentpage,isOnepage):
        """
        获得每个单品首页评论
        inputFilePath ：保存文件路径
        :param items_id: mItemsID
        :param currentpage: 页数
        :return:
        """
        # 构建时间戳 以及 callback
        t_param = time.time()
        t_list = str(t_param).split('.')
        _ksTS = t_list[0] + '_' + t_list[1][:3]
        callback = str(int(t_list[1][:3]) + 1)

        url = 'https://rate.tmall.com/list_detail_rate.htm?'
        # 表头
        headers = {
            'cookie': settings.pcCookie,
            'referer': 'https://detail.tmall.com/item.htm?id={}&on_comment=1'.format(items_id),
            'user-agent': settings.userAgent,
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
        }
        # 构建请求参数
        params = {
            # 商品Id
            'itemId': items_id,
            # 卖家Id
            'sellerId': settings.sEllerId,
            # 爬取评论页面
            'currentPage': currentpage,
            # 时间戳
            "_ksTS": _ksTS,
            # json回调
            "callback": callback,
        }

        try:
            res = requests.get(url, params=params, headers=headers, timeout=30)
            print("开始爬取网页：{}".format(res.url))
            print("状态码：{}".format(res.status_code))
            res.raise_for_status()
            # res.encoding = res.apparent_encoding
            print("爬取内容:{}".format(res.text))
            if isOnepage == 'Y':
                dataProcess.file_input(inputFilePath, 'Comm'+str(items_id), res.text)
            else:
                dataProcess.file_input(inputFilePath, items_id, res.text)
        except:
            print("爬取商品失败!失败ItemID：{}".format(items_id))
            fd = '爬取商品失败!失败ItemID：{}'.format(items_id)
            if isOnepage == 'Y':
                dataProcess.file_input(inputFilePath, 'crawlFailedOnePageCommItems',fd)
            else:
                dataProcess.file_input(inputFilePath, 'crawlFailedAllPageCommItems', fd)

# 测本类
# if __name__ == '__main__':
    # 测试 get_items_comm()
    # inputFilePath = settings.output
    # getOnepageCommFilePath = settings.shopItemsOnePageCommPath
    # fileName = settings.mShopId
    # isOneage = 'Y'
    #
    # crawlerTaobaoComment = CrawlerTaobaoComment()
    #
    # pMItems_id = dataProcess.get_pMItemsInfo_MitemsId(inputFilePath,fileName)
    # # print(items_id)
    # for pMitem_id in pMItems_id:
    #     crawlerTaobaoComment.get_items_comm(getOnepageCommFilePath,pMitem_id,1,isOneage)
    #     time.sleep(25)

    # 商品列表
    # items_id = filePreRegular.read_items()
    # print(items_id)
    # print(len(get_file_name_ls()))
    # fd = get_item_page_ls()
    # item_page_Input(fd)

    # item_pages= item_page_Input_read()
    # print(item_pages)
    # 根据商品id以及总页面数获取评论
    # for item_page in item_pages:
    #     items = item_page.items()
    #     for key, value in items:
    #         for i in range(1, value + 1):
    #             print('items_id:{},page:{}'.format(key, i))
    #             get_one_page_com(item_id=key, currentPage=i)
    #             time.sleep(30)

    # print(fd)

    # with open(r'D:\Project0611\project2020\20200820\ZSJRTaobao\Output\test.json', 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(fd))

    # with open(r'D:\Project0611\project2020\20200820\ZSJRTaobao\Output\test.json', 'r', encoding='utf-8') as f:
    #     fd_r = json.loads(f.read())
    #     for i in fd_r:
    #         i_items = i.items()
    #         for key,values in i_items:
    #             if values != 0:
    #                 print(key,values)






    # print(get_file_name_ls())
    # print(len(set(items_id)))
    # 根据文件名解析第一页评论
    # file_name_lss = get_file_name_ls()

    # 根据item解析文件第一页评论内容 得到item对于页数
    # item_page_ls = []
    # for file_name_ls in file_name_lss:
    #     with open('Input\\Comm' + str(file_name_ls) + '.txt', 'r', encoding='utf-8') as f:
    #         fd = f.read()
    #         fd = re.findall('\\((.*)\\)', fd)
    #         for i in fd:
    #             item_page_dict = {}
    #             i = json.loads(i)
    #             page = i.get('rateDetail').get('paginator').get('lastPage')
    #             # print(page)
    #             item_page_dict[file_name_ls] = page
    #             # print(item_page_dict)
    #             item_page_ls.append(item_page_dict)
    # print(item_page_ls)



        # print(type(item))
        # lastPage = item.get('rateDetail').get('paginator').get('lastPage')
        # print(lastPage)
        # item_lastPage_ls = []
        # item_lastpage = {}
        # for s in fd:
        #     print(s)
        #     print(type(s))
            # item = json.loads(s)
            # print(item)
            # lastPage = item.get('rateDetail').get('paginator').get('lastPage')
            # print(lastPage)
            # item_lastpage[file_name_ls] = lastPage
        # # item_lastPage_ls.append(item_lastpage)
        # # print(item_lastPage_ls)
        #     # print(lastPage)
        # print(item_lastpage )



        # # print(file_name_ls)
        # with open('Input\\Comm'+str(file_name_ls)+'.txt','r',encoding='utf-8') as f:
        #     fd = f.read()
        #     fd = re.findall('\\((.*)\\)', fd)
        #     # fd = json.dumps(fd)
        #     # fd = json.loads(fd)
        #     print(type(fd))
        #     # item_lastPage_ls = []
        #     # item_lastpage = {}
        #     # for s in fd:
        #     #     print(s)
        #     #     # print(type(i))
        #     #     item = json.loads(s)
        #     #     print(item)
        #     #     lastPage = item.get('rateDetail').get('paginator').get('lastPage')
        #     #     item_lastpage[file_name_ls] = lastPage
        #     # # item_lastPage_ls.append(item_lastpage)
        #     # # print(item_lastPage_ls)
        #     #     # print(lastPage)
        #     # print(item_lastpage )
        #     count +=1
        # print(count)


    # 商品item与文件并集
    # not_craw_item = set(items_id) - set(file_name_lss)
    # print(not_craw_item)


    # currentPage = 2
    # for item_id in items_id:
    #     for page in range(1,currentPage):
    #         print(type(item_id),item_id,type(page),page)
    #         get_one_page_com(item_id=item_id,currentPage=page)
    #         time.sleep(30)
    # get_one_page(44386180857,1)





