# _*_ coding:utf-8 _*_
# @FileName : crawlerTaobaoItem.PY
# @time     : 2020/9/7 11:14
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090801
# @UpDate   : 20200910
# @Description:
# 通过手机端获取商品信息并下载保存原始数据

import requests
from settings import Settings
from dataProcess import DataProcess

settings = Settings()
dataProcess = DataProcess()

class CrawlerTaobaoItem:

    def __init__(self):
        self.cookie = settings.mCookie
        self.userAgent = settings.userAgent
        self.shopItemsPath = settings.shopItemsPath
        self.mShopId = settings.mShopId

    def get_mShop_items(self,page):
        '''
        获取M端网页的商品列表
        :param page: 商品列表页数
        :return: 输出商品json格式
        '''
        url = 'https://zhongshunjierou.m.tmall.com/shop/shop_auction_search.do?sort=s&p={}&shop_id={}'.format(page, self.mShopId)
        headers = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': self.cookie ,
            'referer': 'https://zhongshunjierou.m.tmall.com/shop/shop_auction_search.htm?sort=default',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': self.userAgent,
        }
        print('开始爬取网页：{}'.format(url))
        try:
            self.res = requests.get(url, headers=headers)
            self.fd = self.res.text
            print("爬取成功：{}".format(url))
            # self.items_input(mShopId, self.fd)
            dataProcess.file_input(self.shopItemsPath, self.mShopId, self.fd)
        except:
            print('爬取失败：{}'.format(url))
            self.fd = '爬取失败：{}'.format(url)
            # self.items_input(self.shopItemsPath + 'log.txt', self.fd)
            dataProcess.file_input(self.shopItemsPath,'mShopLog',self.fd)


# 测试代码 本类代码
# if __name__ == '__main__':
#     crawlerTaobaoItem = CrawlerTaobaoItem()
#     pages = 2
#     # shop_id = '115842711'
#     for page in range(1,pages):
#         print('第{}页'.format(page))
#         fd = crawlerTaobaoItem.get_mShop_items(page)