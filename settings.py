# _*_ coding:utf-8 _*_
# @FileName : Settings.PY
# @time     : 2020/9/7 15:01
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090801
# @UpDate   : 20200908
# @Description: 参数设置

class Settings():

    def __init__(self):
        # 原始数据文件目录 Input
        # 店铺商品列表路径
        self.shopItemsPath = '..//ZSJRTaobao//Input//shopItems//'
        # 店铺商品列表爬取商品一页评论
        self.shopItemsOnePageCommPath = '..//ZSJRTaobao//Input//shopItemsOnePageComm//'
        # 商品列表所有评论(实际就是99页)
        self.shopItemsAllPageCommPath = '..//ZSJRTaobao//Input//shopItemsAllPageComm//'
        # 数据处理中文件目录
        self.process = '..//SJRTaobao//Process//'
        # 数据处理后输出
        self.output = '..//ZSJRTaobao//Output//'

        # 手机网页版天猫店id
        self.mShopId = 115842711
        # 天猫店销售id
        self.sEllerId = 2328901391

        # 手机网页版天猫店cookie
        self.mCookie = 'yourcookie'
        # PC端天猫店cookie
        self.pcCookie ='yourcookie'

        # u
        self.userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'











